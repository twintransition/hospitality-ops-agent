"""Business lookup functions used by operational workflows.

The workflow layer does not know whether data comes from SQLite, PostgreSQL,
or another source. It only requests business information.
"""

from ..database.sqlite_store import fetch_one


def find_guest(guest_id):
    return fetch_one(
        "SELECT * FROM guests WHERE guest_id = ?",
        (guest_id,),
    )


def find_reservation(reservation_id):
    return fetch_one(
        "SELECT * FROM reservations WHERE reservation_id = ?",
        (reservation_id,),
    )


def get_policy(category):
    policy = fetch_one(
        "SELECT * FROM policies WHERE category = ?",
        (category,),
    )

    if policy is None:
        return None

    policy["late_checkin_allowed"] = True
    return policy
