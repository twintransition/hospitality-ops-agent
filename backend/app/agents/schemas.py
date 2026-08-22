"""Structured outputs used by agents."""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class IntentResult:
    intent: str
    confidence: float
    entities: Dict[str, str] = field(default_factory=dict)
    requires_reservation: bool = False
