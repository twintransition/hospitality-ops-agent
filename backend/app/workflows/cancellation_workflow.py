"""Cancellation workflow.

Keeps operational decisions outside the LLM. The agent identifies the request;
this workflow evaluates reservation and policy information.
"""


def execute_cancellation(context: dict) -> dict:
    reservation_status = context.get("reservation_status", "confirmed")
    policy = context.get("cancellation_policy", "standard")

    if reservation_status == "missing":
        decision = "needs_review"
    elif policy == "non_refundable":
        decision = "needs_review"
    else:
        decision = "cancellation_requested"

    return {
        "workflow": "cancellation",
        "decision": decision,
        "required_actions": ["record_cancellation_request"],
    }
