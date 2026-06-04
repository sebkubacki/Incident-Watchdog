from parser import parse_logs

incidents, devices = parse_logs("../logs/atm.log")

def get_history(selected_device):
    filtered_incidents = [
        incident for incident in incidents
        if incident["device_id"] == selected_device
        ]
    return filtered_incidents

def get_status_count(selected_status):
    status_counter = 0
    for incident in incidents:
        if incident['status'] == selected_status:
            status_counter+=1
    return status_counter

def show_list(list):
    print("\n".join(list))

def show_history():
    while True:
        print("""
        ATM STATUS HISTORY
        Check incidents of any ATM
        If you want to quit type "Exit"
        If you want to see ATM list type "Show list"
        Please enter device ID:
        """)
        selected_device = input()
        if selected_device in devices:
            filtered_incidents = get_history(selected_device)
            device_statuses = "\n".join(
                  f"{incident['timestamp']} | {incident['device_id']} | {incident['status']} | {incident['info']}"
                    for incident in filtered_incidents
                    )
            print(device_statuses)
        elif selected_device.lower() == "show list":
            show_list(devices)
        elif selected_device.lower() == "exit":
            break
        else:
            print("Wrong ATM ID or invalid data entered.")

def count_statuses():
    defined_statuses = ["ERROR", "WARNING", "INFO", "OK"]
    while True:
        print("""
            CHECK ATM STATUS
            Check number of given statuses in incident list
            If you want to quit type "Exit"
            If you want to see status types "Show list"
            Enter status you want to check:
            """)
        selected_status = input().upper()
        if selected_status in defined_statuses:
            status_counter = get_status_count(selected_status)
            print(f"{selected_status}: {status_counter}")
        elif selected_status.lower() == "show list":
            show_list(defined_statuses)
        elif selected_status.lower() == "exit":
            break
        else:
            print("Wrong status name or invalid data entered.")

def top_incidents():
    incident_counter = 1
    incidents_info = {}
    for incident in incidents:
        if incident["status"] in ["ERROR", "WARNING"]:
            incident_name = incident["info"]
            if incident_name not in incidents_info:
                incidents_info[incident_name] = 1
            else:
                incidents_info[incident_name] += 1
    for inc in incidents_info:
        print(f"{inc}: {incidents_info[inc]}")

def detect_instability():
    #todo:  development of instability conditions, check frequency for events, rate instability in %.
    previous_status = None
    current_status = None
    for device in devices:
        status_change = 0
        for inc in incidents:
            if inc["device_id"] == device:
                current_status = inc['status']
                if previous_status != "None":
                    if previous_status is not None:
                        if previous_status == "OK":
                            if current_status == "ERROR":
                                status_change += 3
                            if current_status == "WARNING":
                                status_change += 1
                            if current_status == "INFO":
                                status_change += 1
                        if previous_status == "WARNING":
                            if current_status == "ERROR":
                                status_change += 2
                            if current_status == "OK":
                                status_change += 0
                            if current_status == "INFO":
                                status_change += 1
                        if current_status == "ERROR":
                            if previous_status == "WARNING":
                                status_change += 1
                    previous_status = current_status
        print(f"{device} - status changed {status_change} times")
detect_instability()

            
        
            
