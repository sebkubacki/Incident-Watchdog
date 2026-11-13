# Incident Watchdog

Uruchomienie na macOS:

    cd /Users/sebkub44/Documents/dev/Watchdog
    python3 -m unittest discover -s tests -v
    python3 -m watchdog --seed 7

Menu pokazuje snapshot stanów, odświeżany widok live, łączenie filtrów status/device/module i ostatnią historię z SQLite. Generator działa niezależnie w tle. Domyślne pliki to database/incidents.db i logs/live.log.

Przydatne opcje:

    python3 -m watchdog --min-interval 0.5 --max-interval 2
    python3 -m watchdog --database /tmp/watchdog.db --log /tmp/watchdog.log
