from detector import (
        show_history,
        count_statuses,
        top_incidents,
        detect_instability,
        show_sorted()vim
)



def main_menu(incidents, devices):

    MAIN_MENU = """
========================
 INCIDENT WATCHDOG
========================

1. Show ATM history
2. Count statuses
3. Top incidents
4. Detect instability
5. Show all incidents sorted by time
6. Exit
"""

    while True:

        print(MAIN_MENU)
        choice = input("Select option: ")

        if choice == "1":
            show_history(incidents, devices)

        elif choice == "2":
            count_statuses(incidents)

        elif choice == "3":
            top_incidents(incidents)

        elif choice == "4":
            detect_instability(incidents, devices)

        elif choice == "5":
            show_sorted(incidents)

        elif choice == "6":
            break

        else:
            print("Invalid option")
