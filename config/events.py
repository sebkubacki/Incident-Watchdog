COMMON_MODULES = {
    "NETWORK": {
            "CONNECTION_LOST": "ERROR",
            "HIGH_LATENCY": "WARNING",
            "CONNECTION_STABLE": "OK",
            "PACKET_LOSS_ALERT": "WARNING",
            "MEDIUM_LATENCY": "WARNING",
            "ROUTER_POWER_LOST": "ERROR",
            "ROUTER_POWER_RETURN": "OK"
            },
        "CARD_READER": {
            "FAIL_TO_EJECT_CARD": "ERROR",
            "MCRW_OK_AFTER_RESET": "OK",
            "READ_RETRY_LIMIT": "WARNING",
            "READER_OK": "OK",
            "MOTOR_FAILED": "ERROR"
            },
        "PRINTER": {
            "PAPER_LOW": "WARNING",
            "PAPER_EMPTY": "ERROR",
            "PRINTER_OK": "OK",
            "PRINTER_JAM": "ERROR"
            },   
        "DOOR": {
            "DOOR_OPEN": "WARNING",
            "DOOR_CLOSED": "OK",
            "DOOR_FORCED_OPEN": "ERROR",
            },
        "POWER": {
            "POWER_LOST": "ERROR",
            "UPS_ACTIVE": "WARNING",
            "LOW_BATTERY": "WARNING",
            "POWER_STABLE": "OK"
            },
        "SAFE": {
            "SAFE_OPEN": "WARNING",
            "SAFE_CLOSED": "OK",
            "SAFE_LOCK_FAILURE": "ERROR",
            "SAFE_FORCED_OPEN": "ERROR",
            "SAFE_ACCESS_RESTORED": "OK"
        }
    }
ATM_MODULES = {
        "CASH_DISPENSER": {
            "CASH_JAM": "ERROR",
            "DISPENSER_TIMEOUT": "WARNING",
            "PICK_FAILURE": "WARNING",
            "DISPENSER_OK": "OK",
            "DISPENSER_TRANSPORT_PATH_ERROR": "ERROR"
            },
        "CASH_CASSETTE": {
            "CASSETTE_LOW_LEVEL": "WARNING",
            "CASSETTE_EMPTY": "ERROR",
            "CASSETTE_OK": "OK",
            "CASSETTE_REPELNISHED": "OK",
            "CASSETTE_JAMMED": "ERROR"
            },
        "SHUTTER": {
            "SHUTTER_BLOCKED": "ERROR",
            "SHUTTER_JAMMED_OPEN": "ERROR",
            "SHUTTER_JAMMED_CLOSE": "ERROR",
            "SHUTTER_TIMEOUT": "WARNING",
            "SHUTTER_CLOSED": "OK",
            "SHUTTER_OK_AFTER_RESTART": "OK"
            }
    }

REC_MODULES = {

        "DEPOSIT_MODULE": {
            "TRANSPORT_BLOCKED": "ERROR",
            "NOTE_REJECTED": "WARNING",
            "DEPOSIT_BIN_NEAR_FULL": "WARNING",
            "DEPOSIT_BIM_FULL": "ERROR",
            "DEPOSIT_OK": "OK",
            "DEPOSIT_RECOVERED": "OK"
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
            "RECYCLER_RECOVERED": "OK",
            "RECYCLER_OK": "OK"
        }
    }










