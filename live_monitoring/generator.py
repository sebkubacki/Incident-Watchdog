import random
import time
from datetime import datetime
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

def generate_event():
    rnd_device = get_random_device()
    device_type = get_device_type(rnd_device)
    avalible_modules = get_avalible_modules(device_type)
    rnd_module = get_random_module(avalible_modules)
    events = get_events_for_module(avalible_modules, rnd_module)
    rnd_event = get_random_event(events)
    status = get_status(events, rnd_event)
    timestamp = get_timestamp()
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

generate_log()
