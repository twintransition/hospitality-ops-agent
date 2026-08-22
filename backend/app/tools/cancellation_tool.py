"""Tools for cancellation operations."""


def check_cancellation_policy(reservation_id: str):
    return {
        "reservation_id": reservation_id,
        "policy_status": "eligible",
        "refund_type": "full_review_required",
    }


def request_cancellation(reservation_id: str):
    return {
        "reservation_id": reservation_id,
        "action": "cancellation_requested",
        "status": "pending",
    }
