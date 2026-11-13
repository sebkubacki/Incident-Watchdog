"""Thread-safe live monitoring service built on the existing configuration."""
from __future__ import annotations
import random
import threading
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable
from config.devices import ATM_DEVICES, REC_DEVICES
from config.events import COMMON_MODULES, ATM_MODULES, REC_MODULES
from config.lifecycles import DEFAULT_STATES, MODULE_LIFECYCLES

def timestamp():
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")

def device_type(device):
    if device in ATM_DEVICES:
        return ATM_DEVICES[device]
    return REC_DEVICES[device]

def modules_for(kind):
    if kind == "ATM": return {**COMMON_MODULES, **ATM_MODULES}
    if kind == "REC": return {**COMMON_MODULES, **ATM_MODULES, **REC_MODULES}
    raise ValueError(f"Unknown device type: {kind}")

@dataclass(frozen=True)
class Event:
    device: str
    device_type: str
    module: str
    event: str
    status: str
    timestamp: str
    def as_dict(self): return self.__dict__.copy()

class StateStore:
    def __init__(self):
        self._lock = threading.RLock()
        self._states = {}
        for device in [*ATM_DEVICES, *REC_DEVICES]:
            available = modules_for(device_type(device))
            self._states[device] = {
                module: {"event": event, "status": available[module][event], "timestamp": timestamp()}
                for module, event in DEFAULT_STATES.items() if module in available
            }

    def snapshot(self):
        with self._lock:
            return {d: {m: v.copy() for m, v in modules.items()} for d, modules in self._states.items()}

    def devices(self):
        with self._lock: return list(self._states)

    def transition(self, device, module):
        with self._lock:
            kind = device_type(device)
            available = modules_for(kind)
            current = self._states[device][module]["event"]
            next_event = random.choice(MODULE_LIFECYCLES[module][current])
            result = Event(device, kind, module, next_event, available[module][next_event], timestamp())
            self._states[device][module] = {"event": result.event, "status": result.status, "timestamp": result.timestamp}
            return result

class Generator:
    def __init__(self, store, on_event: Callable[[Event], None], interval=(1.0, 5.0), seed=None):
        self.store, self.on_event, self.interval = store, on_event, interval
        self.random = random.Random(seed)
        self.stop_requested = threading.Event()
        self.thread = None

    def start(self):
        if self.running: return
        self.stop_requested.clear()
        self.thread = threading.Thread(target=self._run, name="incident-generator", daemon=True)
        self.thread.start()

    def stop(self):
        self.stop_requested.set()
        if self.thread: self.thread.join(3)

    @property
    def running(self): return bool(self.thread and self.thread.is_alive())

    def generate_once(self):
        device = self.random.choice(self.store.devices())
        module = self.random.choice(list(modules_for(device_type(device))))
        event = self.store.transition(device, module)
        self.on_event(event)
        return event

    def _run(self):
        while not self.stop_requested.is_set():
            self.generate_once()
            self.stop_requested.wait(self.random.uniform(*self.interval))

def format_event(event):
    data = event.as_dict() if isinstance(event, Event) else event
    return f"{data['device']} | {data['timestamp']} | {data['status']} | {data['module']}: {data['event']}"

def append_log(event, path):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("a", encoding="utf-8") as stream:
        stream.write(format_event(event) + "\n")
