from live_monitoring.generator import device_states, generate_event
from scripts.detector import (
    get_current_device_states,
    show_states,
    filter_by_status,
    filter_by_device,
    filter_by_module,
    get_devices,
    get_modules,
    show_list
)
from scripts.menu import main_menu
import time


while True:

    for _ in range(20):
        generate_event()

    current_states = get_current_device_states(device_states)

    show_states(
        filter_by_status(current_states, "ERROR")
            )

    time.sleep(3)

