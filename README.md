# Incident Watchdog

Incident Watchdog is a Python-based ATM and cash recycler monitoring simulation tool focused on log parsing, incident analysis and automation workflows.

The project simulates a lightweight monitoring and investigation system capable of parsing ATM/REC logs, grouping incidents by device, and analyzing device event history directly from the terminal.

---

# Current Features

- ATM and recycler log parsing
- Incident grouping by device ID
- Interactive incident history lookup
- Terminal-based monitoring workflow
- Modular parser and detector architecture
- Structured event processing using Python dictionaries
- ERROR / WARNING event handling foundation

---

# Planned Features

- Repeated incident detection
- Alert generation and logging
- Incident statistics
- Real-time log watching
- Bash-based fake incident generator
- Configurable alert rules
- Automated incident prioritization
- Recovery detection logic

---

# Technologies

- Python 3
- Bash / Linux terminal
- Git
- JSON
- File-based logging

---

# Project Structure

```text
incident-watchdog/
│
├── logs/          # simulated ATM logs
├── alerts/        # generated alerts
├── config/        # future alert rules/configs
├── scripts/
│   ├── parser.py
│   ├── detector.py
│   ├── menu.py
│   └── main.py
│
├── watchdog/
│
├── README.md
└── .gitignore
```

---

# Current Workflow

1. Parse ATM log entries
2. Clean and structure raw incident data
3. Group incidents by device ID
4. Analyze ATM event history
5. Detect suspicious or important incident patterns
6. Prepare data for future alerting logic

---

# Learning Focus

This project focuses on:

- automation engineering concepts
- monitoring workflows
- log analysis
- incident investigation
- terminal tooling
- Python fundamentals
- modular application design
- system thinking

---

# Project Status

Project currently in active development.

## Implemented Components

- working log parser
- device-based incident grouping
- detector module
- interactive ATM incident history lookup

## Next Development Steps

- incident detection rules
- alert engine
- live monitoring simulation
- automated response workflows# Incident Watchdog

Incident Watchdog is a Python-based ATM and cash recycler monitoring simulation tool designed for learning automation, log processing, and incident detection workflows.

The project simulates a lightweight monitoring engine that analyzes ATM/REC logs, detects incidents, applies alerting rules, and generates alerts based on device activity.

---

## Main Goals

- Learn Python through practical automation use cases
- Understand log parsing and event-driven workflows
- Build monitoring and alerting logic
- Practice Linux terminal and Bash scripting
- Simulate real-world incident management systems

---

## Features (planned)

- ATM and recycler log monitoring
- ERROR/WARNING incident detection
- Repeated incident detection
- Alert generation and logging
- Incident statistics
- Real-time log watching
- Bash-based fake incident generator
- Configurable alert rules

---

## Technologies

- Python 3
- Bash / Linux terminal
- Git
- JSON
- File-based logging

---

## Project Structure

```text
incident-watchdog/
│
├── logs/
├── alerts/
├── config/
├── scripts/
├── watchdog/
│
├── README.md
└── .gitignore
```

---

## Learning Focus

This project focuses on:

- automation engineering concepts
- monitoring workflows
- log analysis
- terminal tooling
- Python fundamentals
- system thinking

---

# Project Status

Project currently in active development.

## Implemented Components

- working log parser
- device-based incident grouping
- detector module
- interactive ATM incident history lookup

## Next Development Steps

- incident detection rules
- alert engine
- live monitoring simulation
- automated response workflows
