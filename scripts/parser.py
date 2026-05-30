#!/usr/bin/env/python 
f = open("../logs/atm.log")

parts = []

#PARSOWANIE DANYCH

for line in f:
	# rodzielamy po "|"
	# usuwamy spacje bo "/ \n"
	parsed_line = [x.strip() for x in line.split("|")]
	
	#pomijamy puste linie
	if len(parsed_line) > 1:
		parts.append(parsed_line)

#TWORZENIE SŁOWNIKA

devices = {}

for part in parts:
	device_id = part[0]
	
	event = part[1:]
	
	if device_id not in devices:
		devices[device_id] = []

	devices[device_id].append(event)

#PRINT

for device in devices:
	print(device)
	print(devices[device])
	print()
		

	
