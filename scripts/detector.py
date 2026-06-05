
def get_history(incidents, selected_device):
    filtered_incidents = [
        incident for incident in incidents
        if incident["device_id"] == selected_device
        ]
    return filtered_incidents

def get_status_count(incidents, selected_status):
    status_counter = 0
    for incident in incidents:
        if incident['status'] == selected_status:
            status_counter+=1
    return status_counter

def show_list(items):
    print("\n".join(items))

def show_history(incidents, devices):
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
            filtered_incidents = get_history(incidents, selected_device)
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

def count_statuses(incidents):
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
            status_counter = get_status_count(incidents, selected_status)
            print(f"{selected_status}: {status_counter}")
        elif selected_status.lower() == "show list":
            show_list(defined_statuses)
        elif selected_status.lower() == "exit":
            break
        else:
            print("Wrong status name or invalid data entered.")

def top_incidents(incidents):
    incident_counter = 1
    incidents_info = {}
    for incident in incidents:
        if incident["status"] in ["ERROR", "WARNING"]:
            incident_name = incident["info"]
            if incident_name not in incidents_info:
                incidents_info[incident_name] = 1
            else:
                incidents_info[incident_name] += 1
    sorted_incidents = sorted(
            incidents_info.items(), 
            key=lambda item: item[1], 
            reverse=True
            )
    for name, count in sorted_incidents:
        print(f"{name}: {count}")

def detect_instability(incidents, devices):
    #todo:  development of instability conditions, check frequency for events, rate instability in %.
    previous_status = None
    current_status = None
    for device in devices:
        previous_status = None
        status_change = 0
        threshold = 3
        for inc in incidents:
            if inc["device_id"] == device:
                current_status = inc['status']
                if previous_status is not None:
                    if current_status != previous_status:
                        status_change += 1
                previous_status = current_status
        if status_change >= threshold:
            print(f"Above threshold: {device} - status changed {status_change} times")
        print(f"{device}: {status_change}")
           
def show_sorted(incidents):
    time_sorted_incidents = sorted(incidents,
                                   key=lambda x: x["timestamp"]
                                   )
    for inc in time_sorted_incidents:
        print(f"{inc} \n")

