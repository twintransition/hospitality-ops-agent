"""Intent to workflow routing layer.

Keeps workflow selection separate from intent detection.
"""


def route_intent(intent: str):
    routes = {
        "late_checkin": "late_checkin_workflow",
    }

    return routes.get(intent)
