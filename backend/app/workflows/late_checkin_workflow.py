"""Late check-in operational workflow.

This is intentionally deterministic before LLM integration.
The workflow validates business steps first, then an AI layer can assist.
"""


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
