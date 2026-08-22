"""Business data lookup functions used by workflows.

The MVP keeps the service layer separate from workflows so the data
source can evolve from seed objects to a production database later.
"""

from ..database.seed import load_seed_data


DATA = load_seed_data()


def find_guest(guest_id):
    return next((g for g in DATA["guests"] if g.guest_id == guest_id), None)


def find_reservation(reservation_id):
    reservation = next(
        (r for r in DATA["reservations"] if r.reservation_id == reservation_id),
        None,
    )
    if reservation is None:
        return None

    return {
        "reservation_id": reservation.reservation_id,
        "guest_id": reservation.guest_id,
        "room_type": reservation.room_type,
        "status": reservation.status,
        "check_in": reservation.check_in,
        "check_out": reservation.check_out,
    }


def get_policy(category):
    policy = next((p for p in DATA["policies"] if p.category == category), None)
    if policy is None:
        return None

    return {
        "category": policy.category,
        "content": policy.content,
        "late_checkin_allowed": True,
    }
