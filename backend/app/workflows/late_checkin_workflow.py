"""Late check-in operational workflow.

This workflow remains deterministic before LLM integration.
The business rules are separated from future AI reasoning.
"""

import uuid

from app.services.lookup_service import find_reservation, get_policy
from app.database.action_store import save_agent_action
from app.database.conversation_store import save_conversation


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

    response = (
        "Your late check-in has been approved. "
        "Check-in instructions will be provided."
        if result["decision"] == "approved"
        else "Your request requires staff review."
    )

    guest_id = reservation.get("guest_id") if reservation else "unknown"

    save_conversation(
        str(uuid.uuid4()),
        guest_id,
        reservation_id,
        guest_message,
        response,
        "late_checkin",
    )

    result["intent"] = "late_checkin"
    result["guest_message"] = guest_message
    result["response"] = response

    return result
