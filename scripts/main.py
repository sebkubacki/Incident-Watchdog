from parser import parse_logs
from menu import main_menu

incidents, devices = parse_logs("../logs/atm.log")

main_menu(incidents, devices)
