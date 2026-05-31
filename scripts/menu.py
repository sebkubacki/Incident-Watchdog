def show_sorted(incidents):
    sorted_incidents = sorted(incidents, key=lambda x: x["timestamp"])
    print(sorted_incidents)

def id_filtered_devices(incidents, devices):
    chosen_id=""
    while chosen_id not in devices:
        print("""Please enter ID of device to see its incidents. 
        Type 'Hint' to see list of avalible devices
        Type 'Stop' to exit
        """)
        chosen_id = input()
        if chosen_id.lower() == "hint":
            print(devices)
        elif chosen_id.lower() == 'stop':
            break
        else:
            print("Incorect data entered")
    filtered_incidents = [i for i in incidents if i["device_id"] == chosen_id]
    print(filtered_incidents)

def status_filtered_devices(incidents):
    chosen_status=""
    statuses=["ERROR", "WARNING", "INFO", "OK"]
    while chosen_status not in statuses:
       print("""Please enter status of incidents you want to see.
       Type 'Hint' to see list of avalible statuses
       Type 'Stop' to exit
       """)
       chosen_status = input()
       if chosen_status.lower() == "hint":
           print(statuses)
       elif chosen_status.lower() == 'stop':
           break
       else:
           print("Incorrect data entered")
    chosen_status=chosen_status.upper()
    filtered_incidents = [i for i in incidents if i["status"] == chosen_status.upper()]
    print(filtered_incidents)


def main_menu(incidents, devices):

    MAIN_MENU = """
=== INCIDENT WATCHDOG ===

1. Sort events
2. Filter by ATM ID
3. Filter by status
4. Count ERROR/WARNING
5. Exit
"""

    while True:

        print(MAIN_MENU)

        user_choice = input("Choose option: ")
        
        if user_choice == "1":
            print("SORTING")
            show_sorted(incidents)
        elif user_choice == "2":
            print("FILTER ID")
            id_filtered_devices(incidents, devices)
        elif user_choice == "3":
            print("FILTER STATUS")
            status_filtered_devices(incidents)
        elif user_choice == "4":
            print("COUNT")

        elif user_choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid option")
