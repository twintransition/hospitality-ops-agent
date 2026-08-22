"""Simple SOP chunking layer.

Designed to be replaced later by embedding-aware chunking.
"""

from app.knowledge.schema import KnowledgeChunk


def chunk_document(source: str, department: str, title: str, content: str):
    sections = [s.strip() for s in content.split("\n\n") if s.strip()]

    return [
        KnowledgeChunk(
            source=source,
            department=department,
            title=title,
            content=section,
            tags=[]
        )
        for section in sections
    ]
