from parser import parse_logs

incidents, devices = parse_logs("../logs/atm.log")


def show_history():
    print("""
    ATM STATUS HISTORY
    Check incidents of any ATM
    Please enter device ID:
    """)
    selected_device = input()
    filtered_incidents = [
            incident for incident in incidents
            if incident["device_id"] == selected_device
    ]
    device_statuses = "\n".join(
            f"{incident['timestamp']} | {incident['device_id']} | {incident['status']} | {incident['info']}"
            for incident in filtered_incidents
    )
    print(device_statuses)

show_history()
