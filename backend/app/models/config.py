"""Runtime model configuration."""

from dataclasses import dataclass


@dataclass
class ModelConfig:
    provider: str = "mock"
    model_name: str = "development"


model_config = ModelConfig()
