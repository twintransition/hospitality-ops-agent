from fastapi import APIRouter

router = APIRouter(prefix="/reservations", tags=["reservations"])


@router.get("/{reservation_id}")
def get_reservation(reservation_id: str):
    return {
        "reservation_id": reservation_id,
        "status": "lookup_placeholder"
    }
