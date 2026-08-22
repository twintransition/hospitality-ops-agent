"""PostgreSQL/pgvector knowledge backend boundary.

This module defines the production retrieval contract. The initial implementation
is intentionally lightweight so deployment can add pgvector without changing
Knowledge Agent interfaces.
"""


class PgVectorKnowledgeStore:
    """Vector store adapter placeholder.

    Expected production flow:
    SOP chunk -> embedding -> PostgreSQL vector column -> similarity search
    """

    def __init__(self, connection=None):
        self.connection = connection

    def add_chunk(self, chunk, embedding):
        """Persist a knowledge chunk and embedding."""
        raise NotImplementedError("Connect PostgreSQL pgvector backend")

    def similarity_search(self, embedding, limit=5):
        """Return nearest knowledge chunks."""
        raise NotImplementedError("Connect pgvector similarity query")
