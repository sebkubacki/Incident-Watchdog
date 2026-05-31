from parser import parse_logs

devices, incidents = parse_logs()

for device_id, events in device.items():
	print(device_id)
	
#	for event in events:
#		print(events)
