from typing import Any, Dict

from .base import ModelProvider


class MockProvider(ModelProvider):
    """Deterministic provider for development and testing."""

    def generate_structured(
        self,
        prompt: str,
        schema: Dict[str, Any],
    ) -> Dict[str, Any]:
        text = prompt.lower()

        if "check" in text and "late" in text:
            return {
                "intent": "late_checkin",
                "confidence": 0.9,
                "entities": {},
            }

        return {
            "intent": "unknown",
            "confidence": 0.3,
            "entities": {},
        }
