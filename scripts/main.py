from menu import main_menu
from parser import parse_logs

incidents, devices = parse_logs("../logs/atm.log")

main_menu(incidents, devices)
