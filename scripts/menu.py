from scripts.detector import (
    get_current_device_states,
    filter_by_status,
    filter_by_device,
    filter_by_module,
    get_devices,
    get_modules,
    show_states,
    show_list
)


def main_menu(device_states):

    MAIN_MENU = """
========================
 INCIDENT WATCHDOG
========================

1. Show current states
2. Filter by status
3. Filter by device
4. Filter by module
5. Exit
"""

    while True:

        print(MAIN_MENU)
        choice = input("Select option: ")

        if choice == "1":
            current_states = get_current_device_states(device_states)
            show_states(current_states)

        elif choice == "2":
            current_states = get_current_device_states(device_states)
            statuses = [
                    "OK",
                    "INFO",
                    "WARNING",
                    "ERROR"
                    ]
            show_list(statuses)
            status_choice = int(input("Select status: "))
            selected_status = statuses[status_choice - 1]
            filtered_states = filter_by_status(current_states, selected_status)
            show_states(filtered_states)

        elif choice == "3":
                current_states = get_current_device_states(device_states)
                devices = get_devices(current_states)
                show_list(devices)
                device_choice = int(input("Select device: "))
                selected_device = devices[device_choice - 1]
                filtered_states = filter_by_device(
                    current_states,
                    selected_device
                )
                show_states(filtered_states)

        elif choice == "4":
            current_states = get_current_states(device_states)
            modules = get_modules(current_states)
            show_list(modules)
            module_choice = int(input("Select module: "))
            selected_module = modules[module_choice - 1]
            filtered_states = filter_by_module(current_states, selected_module)
            show_states(filtered_states)
        elif choice == "5":
            break

        else:
            print("Invalid option")
