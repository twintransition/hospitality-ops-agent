"""Structured output helpers for model responses."""

from dataclasses import dataclass, field


@dataclass
class ModelResponse:
    data: dict = field(default_factory=dict)
    raw: str | None = None
    model: str | None = None
