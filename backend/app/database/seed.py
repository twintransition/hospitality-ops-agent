"""Load small demo data for local workflow testing."""

from .models import Guest, Reservation, Policy


GUESTS = [
    Guest("G001", "John Smith", "john@example.com"),
]


RESERVATIONS = [
    Reservation(
        "R1001",
        "G001",
        "Deluxe Room",
        "confirmed",
        "2026-09-12",
        "2026-09-15",
    )
]


POLICIES = [
    Policy(
        "P001",
        "late_checkin",
        "Late arrivals are accepted for confirmed reservations. Guests should receive arrival instructions."
    )
]


def load_seed_data():
    return {
        "guests": GUESTS,
        "reservations": RESERVATIONS,
        "policies": POLICIES,
    }
