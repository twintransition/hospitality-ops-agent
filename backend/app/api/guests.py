from fastapi import APIRouter

router = APIRouter(prefix="/guests", tags=["guests"])


@router.get("/{guest_id}")
def get_guest(guest_id: str):
    return {
        "guest_id": guest_id,
        "status": "lookup_placeholder"
    }
