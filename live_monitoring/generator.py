import random
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

def generate_event():
    rnd_device = get_random_device()
    device_type = get_device_type(rnd_device)
    avalible_modules = get_avalible_modules(device_type)
    rnd_module = get_random_module(avalible_modules)
    events = get_events_for_module(avalible_modules, rnd_module)
    rnd_event = get_random_event(events)
    status = get_status(events, rnd_event)
    print(f"""
    Device: {rnd_device}
    Type: {device_type}
    Module: {rnd_module}
    Event: {rnd_event}
    Status: {status}
    """)


generate_event()
