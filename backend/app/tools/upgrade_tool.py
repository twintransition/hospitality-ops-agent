"""Tools for room upgrade operations."""


def check_upgrade_availability(room_type: str | None = None):
    return {
        "requested_room_type": room_type,
        "available": True,
    }


def create_upgrade_request(reservation_id: str):
    return {
        "reservation_id": reservation_id,
        "action": "upgrade_requested",
        "status": "pending",
    }
