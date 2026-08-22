"""Knowledge indexing entry point.

The command prepares SOP knowledge for storage. The storage backend can later
be swapped from local development storage to PostgreSQL + pgvector.
"""

from .loader import load_documents
from .chunker import chunk_documents


def build_knowledge_index(path: str):
    documents = load_documents(path)
    chunks = chunk_documents(documents)
    return chunks
