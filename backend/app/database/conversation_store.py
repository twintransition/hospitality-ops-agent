"""Store guest and agent conversation records."""

from .connection import get_connection


def save_conversation(
    conversation_id: str,
    guest_id: str,
    reservation_id: str,
    guest_message: str,
    agent_response: str,
    intent: str,
):
    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO conversations
            (conversation_id, guest_id, reservation_id, guest_message, agent_response, intent)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                conversation_id,
                guest_id,
                reservation_id,
                guest_message,
                agent_response,
                intent,
            ),
        )
        connection.commit()


def list_conversations():
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT * FROM conversations ORDER BY created_at DESC"
        ).fetchall()
        return [dict(row) for row in rows]
