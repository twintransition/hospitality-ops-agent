"""Load demonstration records into the MVP SQLite database."""

from .sqlite_store import get_db_connection
from .schema import initialize_database


def load_demo_records():
    initialize_database()

    with get_db_connection() as conn:
        conn.execute(
            "INSERT OR REPLACE INTO guests VALUES (?, ?, ?)",
            ("G001", "John Smith", "john@example.com"),
        )

        conn.execute(
            "INSERT OR REPLACE INTO reservations VALUES (?, ?, ?, ?, ?, ?)",
            (
                "R1001",
                "G001",
                "Deluxe Room",
                "confirmed",
                "2026-09-12",
                "2026-09-15",
            ),
        )

        conn.execute(
            "INSERT OR REPLACE INTO policies VALUES (?, ?, ?)",
            (
                "P001",
                "late_checkin",
                "Confirmed reservations may request late check-in.",
            ),
        )
