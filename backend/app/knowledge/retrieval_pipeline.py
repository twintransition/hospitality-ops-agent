from app.knowledge.document_loader import load_documents

DOCUMENT_PATH = "backend/app/knowledge/documents"


def build_knowledge_index():
    return load_documents(DOCUMENT_PATH)


def search_documents(query: str):
    documents = build_knowledge_index()

    results = []
    for doc in documents:
        if any(word.lower() in doc["content"].lower() for word in query.split()):
            results.append(doc)

    return results
