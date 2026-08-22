"""Knowledge objects used by the agent layer."""

from dataclasses import dataclass


@dataclass
class KnowledgeDocument:
    title: str
    content: str
    source: str = "internal_sop"
    category: str = "general"


@dataclass
class RetrievedContext:
    documents: list[KnowledgeDocument]

    def as_text(self) -> str:
        return "\n\n".join(
            f"[{doc.title}]\n{doc.content}" for doc in self.documents
        )
