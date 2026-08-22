"""PostgreSQL pgvector repository boundary.

Keeps vector persistence isolated from the Knowledge Agent.
"""


class PgVectorKnowledgeRepository:
    def __init__(self, session=None):
        self.session = session

    def add_chunk(self, chunk):
        """Persist a knowledge chunk with its embedding."""
        raise NotImplementedError("Database session integration pending")

    def similarity_search(self, embedding, limit=5):
        """Retrieve nearest knowledge chunks."""
        raise NotImplementedError("Vector query integration pending")
