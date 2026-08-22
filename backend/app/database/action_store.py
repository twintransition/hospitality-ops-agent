"""Store workflow decisions for audit history."""

from .connection import get_connection


def save_agent_action(reservation_id: str, decision: str, reason: str = ""):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO agent_actions
        (reservation_id, decision, reason)
        VALUES (?, ?, ?)
        """,
        (reservation_id, decision, reason),
    )

    connection.commit()
    connection.close()
