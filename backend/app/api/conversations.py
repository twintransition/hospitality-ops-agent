from fastapi import APIRouter

router = APIRouter(prefix="/conversations", tags=["conversations"])


@router.post("/")
def create_conversation(payload: dict):
    return {
        "conversation_status": "created",
        "message": payload.get("message")
    }
