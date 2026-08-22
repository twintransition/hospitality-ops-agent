"""Late check-in operational workflow.

This workflow remains deterministic before LLM integration.
The business rules are separated from future AI reasoning.
"""

from app.services.lookup_service import find_reservation, get_policy


def evaluate_late_checkin(reservation, policy):
    """Evaluate whether a late check-in can proceed."""

    if reservation.get("status") != "confirmed":
        return {
            "decision": "needs_review",
            "reason": "reservation_not_confirmed"
        }

    if policy.get("late_checkin_allowed"):
        return {
            "decision": "approved",
            "actions": [
                "update_arrival_note",
                "send_checkin_instructions"
            ]
        }

    return {
        "decision": "needs_review",
        "reason": "policy_restriction"
    }


def process_late_checkin(reservation_id: str, guest_message: str):
    """Execute the MVP guest request workflow."""

    reservation = find_reservation(reservation_id)
    policy = get_policy("late_checkin")

    result = evaluate_late_checkin(reservation, policy)
    result["intent"] = "late_checkin"
    result["guest_message"] = guest_message

    return result
