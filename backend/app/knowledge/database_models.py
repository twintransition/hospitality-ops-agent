"""Database-ready models for persistent knowledge chunks.

This module keeps the knowledge layer independent from the agent layer.
The initial implementation is compatible with a future PostgreSQL + pgvector
migration.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class KnowledgeChunkRecord:
    source: str
    department: str
    title: str
    content: str
    metadata: dict
    embedding: list[float] | None = None
    created_at: datetime | None = None
