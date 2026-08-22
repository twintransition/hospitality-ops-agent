"""Late check-in operational workflow.

This workflow remains deterministic before LLM integration.
The business rules are separated from future AI reasoning.
"""

from app.services.lookup_service import find_reservation, get_policy
from app.database.action_store import save_agent_action


def evaluate_late_checkin(reservation, policy):
    """Evaluate whether a late check-in can proceed."""

    if reservation is None:
        return {
            "decision": "needs_review",
            "reason": "reservation_not_found"
        }

    if reservation.get("status") != "confirmed":
        return {
            "decision": "needs_review",
            "reason": "reservation_not_confirmed"
        }

    if policy and policy.get("late_checkin_allowed"):
        return {
            "decision": "approved",
            "actions": [
                "update_arrival_note",
                "send_checkin_instructions"
            ],
            "reason": "late_checkin_policy_satisfied"
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

    save_agent_action(
        reservation_id,
        result["decision"],
        result.get("reason", ""),
    )

    result["intent"] = "late_checkin"
    result["guest_message"] = guest_message

    return result
