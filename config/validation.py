"""Validation of the existing event and lifecycle configuration."""
from config.devices import ATM_DEVICES, REC_DEVICES
from config.events import COMMON_MODULES, ATM_MODULES, REC_MODULES
from config.lifecycles import DEFAULT_STATES, MODULE_LIFECYCLES

def validate_configuration():
    all_events = {**COMMON_MODULES, **ATM_MODULES, **REC_MODULES}
    errors = []
    for module, lifecycle in MODULE_LIFECYCLES.items():
        if module not in all_events: errors.append(f"missing event module: {module}")
        if module not in DEFAULT_STATES: errors.append(f"missing default state: {module}")
        for current, targets in lifecycle.items():
            if current not in all_events.get(module, {}): errors.append(f"unknown current event: {module}.{current}")
            for target in targets:
                if target not in all_events.get(module, {}): errors.append(f"unknown transition target: {module}.{target}")
        if DEFAULT_STATES.get(module) not in lifecycle: errors.append(f"default has no lifecycle: {module}")
    for device, kind in {**ATM_DEVICES, **REC_DEVICES}.items():
        if kind not in {"ATM", "REC"}: errors.append(f"unknown device type: {device}")
    if errors: raise ValueError("Invalid configuration:\n- " + "\n- ".join(errors))
