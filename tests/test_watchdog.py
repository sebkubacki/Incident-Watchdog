import tempfile
import unittest
from pathlib import Path
from config.validation import validate_configuration
from database.repository import Repository
from live_monitoring.service import Generator, StateStore
from scripts.views import filter_states, states_from

class WatchdogTests(unittest.TestCase):
    def test_configuration_is_complete(self):
        validate_configuration()

    def test_combined_filters(self):
        states = states_from(StateStore().snapshot())
        result = filter_states(states, status="OK", device="ATM001", module="NETWORK")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["event"], "CONNECTION_STABLE")

    def test_generator_persists_event(self):
        store, events = StateStore(), []
        generator = Generator(store, events.append, interval=(0, 0), seed=3)
        with tempfile.TemporaryDirectory() as directory:
            repository = Repository(Path(directory) / "incidents.db")
            event = generator.generate_once()
            repository.record(event.as_dict())
            self.assertEqual(repository.count(), 1)
            self.assertEqual(events[0], event)
            repository.close()
