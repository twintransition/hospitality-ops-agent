"""Conversation history API."""

from fastapi import APIRouter

from app.database.conversation_store import list_conversations, save_conversation


router = APIRouter(prefix="/conversations", tags=["conversations"])


@router.post("/")
def create_conversation(payload: dict):
    save_conversation(
        conversation_id=payload.get("conversation_id", "C1001"),
        guest_id=payload.get("guest_id", "G001"),
        reservation_id=payload.get("reservation_id", "R1001"),
        guest_message=payload.get("message", ""),
        agent_response=payload.get("response", ""),
        intent=payload.get("intent", "unknown"),
    )

    return {
        "conversation_status": "created",
        "message": payload.get("message"),
    }


@router.get("")
def get_conversations():
    return list_conversations()
