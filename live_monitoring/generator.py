import random
import time
from datetime import datetime
from config.lifecycles import DEFAULT_STATES, MODULE_LIFECYCLES
from config.devices import ATM_DEVICES, REC_DEVICES
from config.events import COMMON_MODULES, ATM_MODULES, REC_MODULES

def get_random_device():
    atm_devices = list(ATM_DEVICES)
    rec_devices = list(REC_DEVICES)
    devices = atm_devices + rec_devices
    rand_device = random.choice(devices)
    return rand_device

def get_device_type(device):
    if device in list(ATM_DEVICES):
        device_type = ATM_DEVICES[device]
    else:
        device_type = REC_DEVICES[device]
    return device_type

def get_avalible_modules(device_type):
    if device_type == "ATM":
        avalible_modules = COMMON_MODULES | ATM_MODULES
    elif device_type == "REC":
        avalible_modules = COMMON_MODULES | ATM_MODULES| REC_MODULES
    return avalible_modules

def get_random_module(modules):
    modules_list = list(modules)
    rand_module = random.choice(modules_list)
    return rand_module

def get_events_for_module(modules, module):
    events = modules[module]
    return events

def get_random_event(events):
    events_list = list(events)
    rand_event = random.choice(events_list)
    return rand_event

def get_status(events, event):
    status = events[event]
    return status

def get_timestamp():
    now = datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_now

    
def get_next_event(device, module):
    current_event = device_states[device][module]["event"]
    possible_next_events = MODULE_LIFECYCLES[module][current_event]
    next_event = random.choice(possible_next_events)
    return next_event


def generate_event():
    rnd_device = get_random_device()
    device_type = get_device_type(rnd_device)
    avalible_modules = get_avalible_modules(device_type)
    rnd_module = get_random_module(avalible_modules)
    events = get_events_for_module(avalible_modules, rnd_module)
    rnd_event = get_next_event(rnd_device, rnd_module)
    status = get_status(events, rnd_event)
    timestamp = get_timestamp()
    print(device_states[rnd_device][rnd_module])
    device_states[rnd_device][rnd_module]["event"] = rnd_event
    device_states[rnd_device][rnd_module]["status"] = status
    device_states[rnd_device][rnd_module]["timestamp"] = timestamp
    print(device_states[rnd_device][rnd_module])
    log_data = {
            "device": rnd_device,
            "device_type": device_type,
            "module": rnd_module,
            "event": rnd_event,
            "status": status,
            "timestamp": timestamp
        }
    return log_data
    
def format_log_entry(log_data):
    log = f"{log_data['device']} | {log_data['timestamp']} | {log_data['status']} | {log_data['module']}: {log_data['event']}"
    return log

def write_log(log_entry):
    with open("./logs/live.log", "a", encoding="utf-8") as plik:
        plik.write(log_entry)
    

def generate_log():
    while(True):
        log_data = generate_event()
        log_entry = format_log_entry(log_data)
        write_log(log_entry + "\n")
        delay = random.uniform(1, 5)
        time.sleep(delay)

def initialize_device_states():
    devices = list(ATM_DEVICES) + list(REC_DEVICES)
    device_states = {}
    
    for device in devices:
        device_states[device] = {}

        device_type = get_device_type(device)
        modules = get_avalible_modules(device_type)

        for module in modules:
            default_event = DEFAULT_STATES[module]
            device_states[device][module] = {
                    "event": default_event,
                    "status": modules[module][default_event],
                    "timestamp": get_timestamp()
                    }
    return device_states

def get_active_devices(device_states):
    return [
        device
        for device, modules in device_states.items()
        if any(
            data["event"] is not None
            for data in modules.values()
        )
    ]
    

device_states = initialize_device_states()
log_data = generate_event()
print(log_data)
active_devices = get_active_devices(device_states)
print(active_devices)

for _ in range(300):
    print(generate_event())

#if __name__ == "__main__":
#    generate_log()
