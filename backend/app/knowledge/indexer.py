"""Knowledge indexing pipeline."""

from .loader import SOPLoader
from .chunker import chunk_document


class KnowledgeIndexer:
    def __init__(self, store):
        self.store = store
        self.loader = SOPLoader()

    def build_index(self):
        count = 0
        for document in self.loader.load_documents():
            chunks = chunk_document(document)
            for chunk in chunks:
                self.store.add(chunk)
                count += 1
        return {"indexed_chunks": count}
