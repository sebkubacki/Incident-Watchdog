MODULE_LIFECYCLES = {

    "NETWORK": {

        "CONNECTION_STABLE": [
            "MEDIUM_LATENCY",
            "HIGH_LATENCY",
            "PACKET_LOSS_ALERT",
            "CONNECTION_LOST"
        ],

        "MEDIUM_LATENCY": [
            "CONNECTION_STABLE",
            "HIGH_LATENCY",
            "PACKET_LOSS_ALERT",
            "CONNECTION_LOST"
        ],

        "HIGH_LATENCY": [
            "CONNECTION_STABLE",
            "PACKET_LOSS_ALERT",
            "CONNECTION_LOST",
            "MEDIUM_LATENCY"
        ],

        "PACKET_LOSS_ALERT": [
            "CONNECTION_STABLE",
            "CONNECTION_LOST"
        ],

        "CONNECTION_LOST": [
            "CONNECTION_STABLE",
            "ROUTER_POWER_LOST",
            "CONNECTION_LOST"
        ],

        "ROUTER_POWER_LOST": [
            "CONNECTION_STABLE",
            "ROUTER_POWER_LOST"
        ]
    },

    "CARD_READER": {

        "READER_OK": [
            "READ_RETRY_LIMIT",
            "FAIL_TO_EJECT_CARD",
            "MOTOR_FAILED"
        ],

        "READ_RETRY_LIMIT": [
            "READER_OK",
            "FAIL_TO_EJECT_CARD"
        ],

        "FAIL_TO_EJECT_CARD": [
            "MCRW_OK_AFTER_RESET",
            "FAIL_TO_EJECT_CARD"
        ],

        "MOTOR_FAILED": [
            "MCRW_OK_AFTER_RESET",
            "MOTOR_FAILED"
        ],

        "MCRW_OK_AFTER_RESET": [
            "READER_OK"
        ]
    },

    "PRINTER": {

        "PRINTER_OK": [
            "PAPER_LOW",
            "PRINTER_JAM"
        ],

        "PAPER_LOW": [
            "PRINTER_OK",
            "PAPER_EMPTY"
        ],

        "PAPER_EMPTY": [
            "PRINTER_OK",
            "PAPER_EMPTY"
        ],

        "PRINTER_JAM": [
            "PRINTER_OK",
            "PRINTER_JAM"
        ]
    },

    "DOOR": {

        "DOOR_CLOSED": [
            "DOOR_OPEN",
            "DOOR_FORCED_OPEN"
        ],

        "DOOR_OPEN": [
            "DOOR_CLOSED",
            "DOOR_FORCED_OPEN"
        ],

        "DOOR_FORCED_OPEN": [
            "DOOR_CLOSED",
            "DOOR_FORCED_OPEN"
        ]
    },

    "POWER": {

        "POWER_STABLE": [
            "UPS_ACTIVE",
            "POWER_LOST"
        ],

        "UPS_ACTIVE": [
            "POWER_STABLE",
            "LOW_BATTERY",
            "POWER_LOST"
        ],

        "LOW_BATTERY": [
            "POWER_LOST",
            "POWER_STABLE"
        ],

        "POWER_LOST": [
            "POWER_STABLE",
            "POWER_LOST"
        ]
    },

    "SAFE": {

        "SAFE_CLOSED": [
            "SAFE_OPEN",
            "SAFE_LOCK_FAILURE",
            "SAFE_FORCED_OPEN"
        ],

        "SAFE_OPEN": [
            "SAFE_CLOSED"
        ],

        "SAFE_LOCK_FAILURE": [
            "SAFE_ACCESS_RESTORED",
            "SAFE_LOCK_FAILURE"
        ],

        "SAFE_FORCED_OPEN": [
            "SAFE_ACCESS_RESTORED",
            "SAFE_FORCED_OPEN"
        ],

        "SAFE_ACCESS_RESTORED": [
            "SAFE_CLOSED"
        ]
    },

    "CASH_DISPENSER": {

        "DISPENSER_OK": [
            "DISPENSER_TIMEOUT",
            "PICK_FAILURE",
            "CASH_JAM",
            "DISPENSER_TRANSPORT_PATH_ERROR"
        ],

        "DISPENSER_TIMEOUT": [
            "DISPENSER_OK",
            "PICK_FAILURE"
        ],

        "PICK_FAILURE": [
            "DISPENSER_OK",
            "CASH_JAM"
        ],

        "CASH_JAM": [
            "DISPENSER_OK",
            "CASH_JAM"
        ],

        "DISPENSER_TRANSPORT_PATH_ERROR": [
            "DISPENSER_OK",
            "DISPENSER_TRANSPORT_PATH_ERROR"
        ]
    },

    "CASH_CASSETTE": {

        "CASSETTE_OK": [
            "CASSETTE_LOW_LEVEL"
        ],

        "CASSETTE_LOW_LEVEL": [
            "CASSETTE_OK",
            "CASSETTE_EMPTY"
        ],

        "CASSETTE_EMPTY": [
            "CASSETTE_REPELNISHED",
            "CASSETTE_EMPTY"
        ],

        "CASSETTE_REPELNISHED": [
            "CASSETTE_OK"
        ],

        "CASSETTE_JAMMED": [
            "CASSETTE_OK",
            "CASSETTE_JAMMED"
        ]
    },

    "SHUTTER": {

        "SHUTTER_CLOSED": [
            "SHUTTER_TIMEOUT",
            "SHUTTER_BLOCKED",
            "SHUTTER_JAMMED_OPEN",
            "SHUTTER_JAMMED_CLOSE"
        ],

        "SHUTTER_TIMEOUT": [
            "SHUTTER_CLOSED",
            "SHUTTER_BLOCKED"
        ],

        "SHUTTER_BLOCKED": [
            "SHUTTER_OK_AFTER_RESTART",
            "SHUTTER_BLOCKED"
        ],

        "SHUTTER_JAMMED_OPEN": [
            "SHUTTER_OK_AFTER_RESTART",
            "SHUTTER_JAMMED_OPEN"
        ],

        "SHUTTER_JAMMED_CLOSE": [
            "SHUTTER_OK_AFTER_RESTART",
            "SHUTTER_JAMMED_CLOSE"
        ],

        "SHUTTER_OK_AFTER_RESTART": [
            "SHUTTER_CLOSED"
        ]
    }
}
