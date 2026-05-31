#!/usr/bin/env python3

def parse_logs(path):

    parts = []
    events= []

    # PARSOWANIE DANYCH
    with open(path) as f:

        for line in f:

            # rozdzielamy po "|"
            # usuwamy spacje i \n
            parsed_line = [x.strip() for x in line.split("|")]

            # pomijamy puste linie
            if len(parsed_line) > 1:
                parts.append(parsed_line)

    # TWORZENIE SŁOWNIKA
    devices = {}

    for part in parts:

        device_id = part[0]

        event = part[1:]

        print(events)

        if device_id not in devices:
            devices[device_id] = []

        devices[device_id].append(event)
        


    return devices
