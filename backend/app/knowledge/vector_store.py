"""Vector store abstraction.

Current implementation keeps retrieval backend independent.
Future backends:
- pgvector
- qdrant
- chroma
"""

from app.knowledge.schema import KnowledgeChunk


class KnowledgeStore:
    def __init__(self):
        self.chunks = []

    def add(self, chunks: list[KnowledgeChunk]):
        self.chunks.extend(chunks)

    def search(self, query: str, limit: int = 5):
        query_terms = set(query.lower().split())

        scored = []
        for chunk in self.chunks:
            score = len(
                query_terms.intersection(
                    chunk.content.lower().split()
                )
            )
            scored.append((score, chunk))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [item[1] for item in scored[:limit] if item[0] > 0]
