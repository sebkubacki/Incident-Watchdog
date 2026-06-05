COMMON_MODULE = {
    "NETWORK": {
            "CONNECTION_LOST": "ERROR",
            "HIGH_LATENCY": "WARNING",
            "CONNECTION_RESTORED" : "INFO",
            "CONNECTION_STABLE": "OK",
            "PING_SUCCESFULL": "OK",
            "PACKET_LOST_ALERT": "WARNING",
            "MEDIUM_LATENCY": "WARNING"
            "ROUTER_POWER_LOST": "ERROR",
            "ROUTER_POWER_RETURN": "OK"
            },
        "CARD_READER": {
            "FAIL_TO_EJECT_CARD": "ERROR",
            "MCRW_OK_AFTER_RESET": "INFO",
            "READ_RETRY_LIMIT": "WARNING",
            "READER_OK": "INFO",
            "READ_OK_AFTER_READ_PROBLEM": "OK",
            "MOTOR_FAILED": "ERROR"
            },
        "PRINTER": {
            "PAPER_LOW": "WARNING",
            "PAPER_EMPTY": "ERROR",
            "PAPER_REPLACED": "INFO",
            "PRINTER_OK": "OK",
            "PRINTER_COVER_OPEN": "WARNING",
            "PRINTER_COVER_CLOSED": "INFO",
            "PRINTER_JAM": "ERROR"
            },   
        "DOOR": {
            "DOOR_OPEN": "WARNING",
            "DOOR_CLOSED": "OK",
            "DOOR_FORCED_OPEN": "ERROR",
            "DOOR_SENSOR_FAILURE": "ERROR",
            "DOOR_ALARM_TRIGGERED": "ERROR"
            },
        "POWER": {
            "POWER_LOST": "ERROR",
            "UPS_ACTIVE": "WARNING",
            "LOW_BATTERY": "WARNING",
            "POWER_RESTORED": "INFO",
            "POWER_STABLE": "OK"
            },
        "SAFE": {
            "SAFE_OPEN": "WARNING",
            "SAFE_CLOSED": "OK",
            "SAFE_LOCK_FAILURE": "ERROR",
            "SAFE_FORCED_OPEN": "ERROR",
            "SAFE_ACCESS_RESTORED": "INFO"
        }
    }
ATM_MODULES = (
        "CASH_DISPENSER": {
            "CASH_JAM": "ERROR",
            "DISPENSER_TIMEOUT": "ERROR",
            "PICK_FAILURE": "WARNING",
            "DOUBLE_NOTE_DETECTED": "WARNING",
            "LOW_CASH": "WARNING",
            "CASSETTE_EMPTY": "ERROR",
            "DISPENSER_OK": "OK",
            "DISPENSER_RECOVERED": "INFO"
            },
        "CASH_CASSETTE": {
            "CASSETTE_REMOVED": "WARNING",
            "CASSETTE_INSERTED": "INFO",
            "CASSETTE_LOW_LEVEL": "WARNING",
            "CASSETTE_EMPTY": "ERROR",
            "CASSETTE_LOCK_ERROR": "ERROR",
            "CASSETTE_OK": "OK"
            },
        "SHUTTER": {
            "SHUTTER_BLOCKED": "ERROR",
            "SHUTTER_OPEN_TIMEOUT": "WARNING",
            "SHUTTER_CLOSE_TIMEOUT": "WARNING",
            "SHUTTER_OPEN": "INFO",
            "SHUTTER_CLOSED": "OK",
            "SHUTTER_RECOVERED": "INFO"
            }
    }

RECYCLER_MODULES = {

        "DEPOSIT_MODULE": {
            "TRANSPORT_BLOCKED": "ERROR",
            "DEPOSIT_TIMEOUT": "ERROR",
            "NOTE_REJECTED": "WARNING",
            "DEPOSIT_BIN_NEAR_FULL": "WARNING",
            "DEPOSIT_OK": "OK",
            "DEPOSIT_RECOVERED": "INFO"
        },
        "ESCROW": {
            "ESCROW_FULL": "ERROR",
            "ESCROW_JAM": "ERROR",
            "ESCROW_NEAR_CAPACITY": "WARNING",
            "ESCROW_CLEARED": "INFO",
            "ESCROW_OK": "OK"
        },
        "REJECT_BIN": {
            "BIN_FULL": "ERROR",
            "BIN_NEAR_FULL": "WARNING",
            "BIN_REMOVED": "WARNING",
            "BIN_INSERTED": "INFO",
            "BIN_EMPTY": "OK"
        },
        "CASH_RECYCLER": {
            "RECYCLER_JAM": "ERROR",
            "NOTE_PATH_BLOCKED": "ERROR",
            "CASSETTE_MISMATCH": "ERROR",
            "LOW_RECYCLING_CASH": "WARNING",
            "RECYCLER_SYNC_REQUIRED": "WARNING",
            "RECYCLER_RECOVERED": "INFO",
            "RECYCLER_OK": "OK"
        }
    }










