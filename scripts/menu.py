from detector import (
        show_history,
        count_statuses,
        top_incidents,
        detect_instability
)

def show_sorted(incidents):
    sorted_incidents = sorted(incidents, key=lambda x: x["timestamp"])
    print(sorted_incidents)



def main_menu():

    MAIN_MENU = """
========================
 INCIDENT WATCHDOG
========================

1. Show ATM history
2. Count statuses
3. Top incidents
4. Detect instability
5. Exit
"""

    while True:

        print(MAIN_MENU)
        choice = input("Select option: ")

        if choice == "1":
            show_history()

        elif choice == "2":
            count_statuses()

        elif choice == "3":
            top_incidents()

        elif choice == "4":
            detect_instability()

        elif choice == "5":
            break

        else:
            print("Invalid option")
