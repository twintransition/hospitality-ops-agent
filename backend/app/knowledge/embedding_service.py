"""Embedding service boundary for RAG pipeline."""


class EmbeddingService:
    def __init__(self, provider=None):
        self.provider = provider

    def embed(self, text: str):
        """Generate embedding vector for text.

        Production providers can be OpenAI, BGE, E5, or local embedding models.
        """
        if self.provider:
            return self.provider.embed(text)

        raise NotImplementedError("Configure embedding provider")
