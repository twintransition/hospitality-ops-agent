"""LLM provider abstraction.

Keeps agent logic independent from a specific model vendor.
"""

from abc import ABC, abstractmethod


class ModelProvider(ABC):
    @abstractmethod
    def generate_structured(self, prompt: str, schema: dict):
        """Generate schema-constrained output."""
        raise NotImplementedError


class MockModelProvider(ModelProvider):
    """Local development provider used before connecting external models."""

    def generate_structured(self, prompt: str, schema: dict):
        return {}
