"""Agent execution trace utilities.

Production agents require visibility into intermediate steps.
"""

from datetime import datetime


def add_trace(state, component: str, event: str, data=None):
    state.trace.append(
        {
            "timestamp": datetime.utcnow().isoformat(),
            "component": component,
            "event": event,
            "data": data or {},
        }
    )

    return state
