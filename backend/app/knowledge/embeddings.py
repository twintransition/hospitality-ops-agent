"""Embedding provider abstraction for knowledge retrieval.

The first implementation keeps embeddings replaceable so hosted models or
local embedding models can be introduced without changing retrieval logic.
"""


class EmbeddingProvider:
    def embed(self, text: str) -> list[float]:
        raise NotImplementedError


class MockEmbeddingProvider(EmbeddingProvider):
    """Deterministic placeholder used for development/testing."""

    def embed(self, text: str) -> list[float]:
        values = [float((ord(c) % 10) / 10) for c in text[:16]]
        return values + [0.0] * (16 - len(values))
