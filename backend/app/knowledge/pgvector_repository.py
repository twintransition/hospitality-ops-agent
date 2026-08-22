"""PostgreSQL/pgvector repository boundary.

This is the persistence contract for semantic knowledge retrieval.
The concrete database implementation can be added without changing agents.
"""


class PgVectorKnowledgeRepository:
    def __init__(self, session=None):
        self.session = session

    def add_chunk(self, chunk):
        raise NotImplementedError("Connect PostgreSQL pgvector backend")

    def similarity_search(self, embedding, limit=5):
        raise NotImplementedError("Connect pgvector similarity query")
