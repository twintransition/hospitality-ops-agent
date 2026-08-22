"""Agent graph transition rules."""


INTENT_TO_WORKFLOW = {
    "late_checkin": "late_checkin_workflow",
}


def next_step(intent: str) -> str:
    return INTENT_TO_WORKFLOW.get(intent, "human_review")
