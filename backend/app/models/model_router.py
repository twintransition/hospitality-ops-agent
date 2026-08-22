from .providers import MockProvider, ModelProvider


class ModelRouter:
    """Central model access point for agents."""

    def __init__(self, provider: ModelProvider | None = None):
        self.provider = provider or MockProvider()

    def structured_call(self, prompt: str, schema: dict):
        return self.provider.generate_structured(prompt, schema)


model_router = ModelRouter()
