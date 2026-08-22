"""Intent routing agent.

MVP implementation uses a controlled classifier interface.
A model provider can be attached later without changing workflows.
"""

from .schemas import IntentResult


class IntentAgent:
    def classify(self, message: str) -> IntentResult:
        text = message.lower()

        if "late" in text or "midnight" in text or "flight" in text:
            return IntentResult(
                intent="late_checkin",
                confidence=0.90,
                entities={"source": "guest_message"},
                requires_reservation=True,
            )

        return IntentResult(
            intent="general_request",
            confidence=0.50,
            entities={},
            requires_reservation=False,
        )
