"""SQLite schema creation for the MVP operational database."""

from .connection import get_connection


SCHEMA = """
CREATE TABLE IF NOT EXISTS guests (
    guest_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT
);

CREATE TABLE IF NOT EXISTS reservations (
    reservation_id TEXT PRIMARY KEY,
    guest_id TEXT NOT NULL,
    room_type TEXT,
    status TEXT,
    check_in TEXT,
    check_out TEXT
);

CREATE TABLE IF NOT EXISTS policies (
    policy_id TEXT PRIMARY KEY,
    category TEXT NOT NULL,
    content TEXT NOT NULL,
    late_checkin_allowed INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS conversations (
    conversation_id TEXT PRIMARY KEY,
    guest_id TEXT,
    reservation_id TEXT,
    guest_message TEXT,
    agent_response TEXT,
    intent TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS agent_actions (
    action_id TEXT PRIMARY KEY,
    reservation_id TEXT,
    decision TEXT,
    reason TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
"""


def initialize_database():
    with get_connection() as connection:
        connection.executescript(SCHEMA)
