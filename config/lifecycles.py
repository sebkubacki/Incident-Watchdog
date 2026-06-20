DEFAULT_STATES = {

    "NETWORK": "CONNECTION_STABLE",
    "CARD_READER": "READER_OK",
    "PRINTER": "PRINTER_OK",
    "DOOR": "DOOR_CLOSED",
    "POWER": "POWER_STABLE",
    "SAFE": "SAFE_CLOSED",

    "CASH_DISPENSER": "DISPENSER_OK",
    "CASH_CASSETTE": "CASSETTE_OK",
    "SHUTTER": "SHUTTER_CLOSED",

    "DEPOSIT_MODULE": "DEPOSIT_OK",
    "ESCROW": "ESCROW_OK",
    "REJECT_BIN": "BIN_EMPTY",
    "CASH_RECYCLER": "RECYCLER_OK"
}


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
    },

    "REJECT_BIN": {

        "BIN_EMPTY": [
            "BIN_NEAR_FULL",
            "BIN_REMOVED"
        ],

        "BIN_NEAR_FULL": [
            "BIN_EMPTY",
            "BIN_FULL"
        ],

        "BIN_FULL": [
            "BIN_FULL",
            "BIN_EMPTY"
        ],

        "BIN_REMOVED": [
            "BIN_INSERTED"
        ],

        "BIN_INSERTED": [
            "BIN_EMPTY"
        ]
    },

    "DEPOSIT_MODULE": {

        "DEPOSIT_OK": [
            "NOTE_REJECTED",
            "DEPOSIT_BIN_NEAR_FULL",
            "TRANSPORT_BLOCKED"
        ],

        "NOTE_REJECTED": [
            "DEPOSIT_OK",
            "NOTE_REJECTED",
            "TRANSPORT_BLOCKED"
        ],

        "DEPOSIT_BIN_NEAR_FULL": [
            "DEPOSIT_OK",
            "DEPOSIT_BIM_FULL"
        ],

        "DEPOSIT_BIM_FULL": [
            "DEPOSIT_BIM_FULL",
            "DEPOSIT_RECOVERED"
        ],

        "TRANSPORT_BLOCKED": [
            "TRANSPORT_BLOCKED",
            "DEPOSIT_RECOVERED"
        ],

        "DEPOSIT_RECOVERED": [
            "DEPOSIT_OK"
        ]
    },

    "ESCROW": {

        "ESCROW_OK": [
            "ESCROW_NEAR_CAPACITY",
            "ESCROW_JAM"
        ],

        "ESCROW_NEAR_CAPACITY": [
            "ESCROW_OK",
            "ESCROW_FULL",
            "ESCROW_JAM"
        ],

        "ESCROW_FULL": [
            "ESCROW_FULL",
            "ESCROW_CLEARED"
        ],

        "ESCROW_JAM": [
            "ESCROW_JAM",
            "ESCROW_CLEARED"
        ],

        "ESCROW_CLEARED": [
            "ESCROW_OK"
        ]
    },

    "CASH_RECYCLER": {

        "RECYCLER_OK": [
            "LOW_RECYCLING_CASH",
            "RECYCLER_SYNC_REQUIRED",
            "NOTE_PATH_BLOCKED",
            "RECYCLER_JAM"
        ],

        "LOW_RECYCLING_CASH": [
            "RECYCLER_OK",
            "CASSETTE_MISMATCH",
            "RECYCLER_SYNC_REQUIRED"
        ],

        "RECYCLER_SYNC_REQUIRED": [
            "RECYCLER_OK",
            "RECYCLER_JAM",
            "CASSETTE_MISMATCH"
        ],

        "NOTE_PATH_BLOCKED": [
            "NOTE_PATH_BLOCKED",
            "RECYCLER_RECOVERED"
        ],

        "RECYCLER_JAM": [
            "RECYCLER_JAM",
            "RECYCLER_RECOVERED"
        ],

        "CASSETTE_MISMATCH": [
            "CASSETTE_MISMATCH",
            "RECYCLER_RECOVERED"
        ],

        "RECYCLER_RECOVERED": [
            "RECYCLER_OK"
        ]
    }
}
