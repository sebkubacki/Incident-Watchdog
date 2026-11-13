"""Snapshot, combined filters and terminal presentation."""
def states_from(snapshot):
    return [{"device": d, "module": m, **data} for d, modules in snapshot.items() for m, data in modules.items()]

def filter_states(states, status=None, device=None, module=None):
    return [dict(s) for s in states if (status is None or s["status"] == status) and (device is None or s["device"] == device) and (module is None or s["module"] == module)]

def show_states(states):
    states = sorted(states, key=lambda s: (s["device"], s["module"]))
    print(f"{'DEVICE':<8} {'STATUS':<8} {'MODULE':<20} {'EVENT':<32} TIMESTAMP")
    print("-" * 105)
    for s in states: print(f"{s['device']:<8} {s['status']:<8} {s['module']:<20} {s['event']:<32} {s['timestamp']}")
    print(f"\n{len(states)} state(s)")

def choose(items, prompt):
    for i, item in enumerate(items, 1): print(f"{i}. {item}")
    try: return items[int(input(prompt)) - 1]
    except (ValueError, IndexError): print("Invalid selection."); return None
