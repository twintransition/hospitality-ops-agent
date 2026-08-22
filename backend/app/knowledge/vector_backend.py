"""Vector retrieval backend abstraction.

This keeps the Knowledge Agent independent from the storage engine.
The production implementation can use PostgreSQL + pgvector.
"""


class VectorBackend:
    def add(self, chunks: list[dict]):
        raise NotImplementedError

    def similarity_search(self, embedding: list[float], limit: int = 3):
        raise NotImplementedError


class InMemoryVectorBackend(VectorBackend):
    def __init__(self):
        self.items = []

    def add(self, chunks: list[dict]):
        self.items.extend(chunks)

    def similarity_search(self, embedding: list[float], limit: int = 3):
        return self.items[:limit]
