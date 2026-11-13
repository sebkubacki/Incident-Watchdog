"""Command-line application runner."""
from __future__ import annotations
import argparse
import time
from config.validation import validate_configuration
from database.repository import Repository
from live_monitoring.service import Generator, StateStore, append_log
from scripts.views import filter_states, show_states, states_from, choose

def render(store, status=None, device=None, module=None):
    show_states(filter_states(states_from(store.snapshot()), status, device, module))

def live_view(store, seconds):
    end = time.monotonic() + seconds
    try:
        while time.monotonic() < end:
            print("\033[2J\033[H", end="")
            render(store)
            time.sleep(1)
    except KeyboardInterrupt:
        pass

def menu(store, repository):
    while True:
        print("\n=== INCIDENT WATCHDOG ===")
        print("1. Current states\n2. Live view\n3. Combined filters\n4. Recent history\n5. Exit")
        choice = input("Select option: ").strip()
        if choice == "1":
            render(store)
        elif choice == "2":
            try: seconds = max(1, int(input("Duration [10]: ") or "10"))
            except ValueError: seconds = 10
            live_view(store, seconds)
        elif choice == "3":
            status = input("Status (blank = any): ").strip().upper() or None
            states = states_from(store.snapshot())
            device = choose(sorted({s["device"] for s in states}), "Device number: ") if input("Filter device? [y/N] ").lower() == "y" else None
            module = choose(sorted({s["module"] for s in states}), "Module number: ") if input("Filter module? [y/N] ").lower() == "y" else None
            render(store, status, device, module)
        elif choice == "4":
            for row in repository.recent():
                print(f"{row['timestamp']} | {row['device_id']} | {row['status']} | {row['module']}: {row['event']}")
        elif choice == "5":
            return
        else:
            print("Invalid option.")

def main(argv=None):
    parser = argparse.ArgumentParser(description="ATM and recycler incident watchdog")
    parser.add_argument("--database", default="database/incidents.db")
    parser.add_argument("--log", default="logs/live.log")
    parser.add_argument("--min-interval", type=float, default=1.0)
    parser.add_argument("--max-interval", type=float, default=5.0)
    parser.add_argument("--seed", type=int)
    args = parser.parse_args(argv)
    if args.min_interval < 0 or args.max_interval < args.min_interval:
        parser.error("intervals must satisfy 0 <= min <= max")
    validate_configuration()
    store = StateStore()
    repository = Repository(args.database)
    def persist(event):
        repository.record(event.as_dict())
        append_log(event, args.log)
    generator = Generator(store, persist, (args.min_interval, args.max_interval), args.seed)
    generator.start()
    try:
        menu(store, repository)
    except (EOFError, KeyboardInterrupt):
        print("\nStopping Incident Watchdog.")
    finally:
        generator.stop()
        repository.close()
