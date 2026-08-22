"""Agent action history endpoints."""

from fastapi import APIRouter

from app.database.connection import get_connection

router = APIRouter(prefix="/agent-actions", tags=["agent-actions"])


@router.get("")
def list_actions():
    connection = get_connection()
    cursor = connection.cursor()

    rows = cursor.execute(
        """
        SELECT id, reservation_id, decision, reason, created_at
        FROM agent_actions
        ORDER BY id DESC
        """
    ).fetchall()

    connection.close()

    return [dict(row) for row in rows]
