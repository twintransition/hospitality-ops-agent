"""Room upgrade workflow."""


def execute_room_upgrade(context: dict) -> dict:
    availability = context.get("upgrade_available", False)
    membership = context.get("guest_status", "standard")

    if availability:
        decision = "upgrade_available"
    elif membership == "vip":
        decision = "needs_review"
    else:
        decision = "upgrade_unavailable"

    return {
        "workflow": "room_upgrade",
        "decision": decision,
        "required_actions": ["notify_guest"],
    }
