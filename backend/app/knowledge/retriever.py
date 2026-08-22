"""SOP retrieval abstraction.

This intentionally starts simple. The interface is designed so a vector
retriever can replace the implementation later without changing agents.
"""

from .models import KnowledgeDocument, RetrievedContext


DOCUMENTS = [
    KnowledgeDocument(
        title="Late Check-in SOP",
        category="front_desk",
        content=(
            "Guests arriving after midnight may be accommodated when a valid "
            "reservation exists. Front desk should verify reservation details "
            "and provide arrival instructions."
        ),
    )
]


def retrieve(query: str) -> RetrievedContext:
    query_lower = query.lower()
    matches = [
        doc for doc in DOCUMENTS
        if any(word in query_lower for word in doc.content.lower().split())
        or "check" in query_lower
    ]
    return RetrievedContext(documents=matches or DOCUMENTS[:1])
