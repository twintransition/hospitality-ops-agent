from abc import ABC, abstractmethod
from typing import Any, Dict


class ModelProvider(ABC):
    """Provider interface separating agents from model vendors."""

    @abstractmethod
    def generate_structured(
        self,
        prompt: str,
        schema: Dict[str, Any],
    ) -> Dict[str, Any]:
        raise NotImplementedError
