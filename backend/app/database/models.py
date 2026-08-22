"""Simple MVP data models.

These represent the minimum operational context needed for the
Guest Communication Agent.
"""

from dataclasses import dataclass


@dataclass
class Guest:
    guest_id: str
    name: str
    email: str


@dataclass
class Reservation:
    reservation_id: str
    guest_id: str
    room_type: str
    status: str
    check_in: str
    check_out: str


@dataclass
class Policy:
    policy_id: str
    category: str
    content: str


@dataclass
class AgentAction:
    action_id: str
    reservation_id: str
    decision: str
    reason: str
