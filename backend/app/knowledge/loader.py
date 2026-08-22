"""Knowledge document loading utilities."""

from pathlib import Path

from .schema import KnowledgeChunk


class SOPLoader:
    def __init__(self, document_path=None):
        self.document_path = Path(document_path or Path(__file__).parent / "documents")

    def load_documents(self):
        documents = []
        for file_path in self.document_path.glob("*.md"):
            documents.append(self._load_file(file_path))
        return documents

    def _load_file(self, file_path):
        content = file_path.read_text(encoding="utf-8")
        return {
            "source": file_path.name,
            "content": content,
            "department": self._infer_department(file_path.name),
        }

    def _infer_department(self, filename):
        name = filename.lower()
        if "checkin" in name:
            return "front_desk"
        if "housekeeping" in name:
            return "housekeeping"
        if "upgrade" in name:
            return "front_desk"
        return "general"
