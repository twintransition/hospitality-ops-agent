"""Knowledge document schemas for SOP grounding."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class KnowledgeChunk:
    source: str
    department: str
    title: str
    content: str
    tags: List[str] = field(default_factory=list)


@dataclass
class RetrievedContext:
    query: str
    chunks: List[KnowledgeChunk]
    confidence: float = 0.0
