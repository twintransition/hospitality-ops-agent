from pathlib import Path


def load_documents(folder: str):
    documents = []
    path = Path(folder)

    if not path.exists():
        return documents

    for file in path.glob("*.md"):
        documents.append({
            "title": file.stem,
            "content": file.read_text(encoding="utf-8")
        })

    return documents
