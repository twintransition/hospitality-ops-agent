"""Reservation tools.

Agent-facing interface for reservation operations.
The agent does not know database implementation details.
"""

from app.services.lookup_service import find_reservation


def lookup_reservation(reservation_id: str):
    """Retrieve reservation context for an agent workflow."""
    return find_reservation(reservation_id)
