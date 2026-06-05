#!/usr/bin/env python3

def parse_logs(path):

    parts = []
    events = []

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
    incidents = []
    devices = set()
    for part in parts:

        incident = {
            "device_id": part[0],
            "timestamp": part[1],
            "status": part[2],
            "info": part[3]
        }
        incidents.append(incident)
        
        devices.add(part[0])
    
    return incidents, devices

