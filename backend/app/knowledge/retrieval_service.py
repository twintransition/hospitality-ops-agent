"""Knowledge retrieval service used by agents."""

from .vector_store import KnowledgeStore


class KnowledgeRetrievalService:
    def __init__(self, store=None):
        self.store = store or KnowledgeStore()

    def retrieve(self, query, limit=3):
        results = self.store.search(query, limit=limit)
        return {
            "query": query,
            "chunks": results,
            "confidence": 1.0 if results else 0.0,
        }
