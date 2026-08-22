"""Intent routing agent.

Uses the model layer for structured classification while preserving
workflow control outside the LLM.
"""

from .schemas import IntentResult
from app.models.model_router import model_router


INTENT_SCHEMA = {
    "type": "object",
    "properties": {
        "intent": {"type": "string"},
        "confidence": {"type": "number"},
        "entities": {"type": "object"},
        "requires_reservation": {"type": "boolean"},
    },
    "required": [
        "intent",
        "confidence",
        "entities",
        "requires_reservation",
    ],
}


class IntentAgent:
    def classify(self, message: str) -> IntentResult:
        prompt = f"""
Classify the hospitality guest request.

Allowed intents:
- late_checkin
- cancellation
- room_upgrade
- housekeeping
- complaint
- general_request

Guest message:
{message}

Return only structured data.
"""

        result = model_router.structured_call(prompt, INTENT_SCHEMA)

        return IntentResult(
            intent=result.get("intent", "general_request"),
            confidence=float(result.get("confidence", 0.0)),
            entities=result.get("entities", {}),
            requires_reservation=bool(result.get("requires_reservation", False)),
        )
