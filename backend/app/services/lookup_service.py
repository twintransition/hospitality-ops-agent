"""Business data lookup functions used by workflows."""

from ..database.seed import load_seed_data


DATA = load_seed_data()


def find_guest(guest_id):
    return next((g for g in DATA["guests"] if g.guest_id == guest_id), None)


def find_reservation(reservation_id):
    return next((r for r in DATA["reservations"] if r.reservation_id == reservation_id), None)


def get_policy(category):
    return next((p for p in DATA["policies"] if p.category == category), None)
