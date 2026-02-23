from dataclasses import dataclass
from datetime import datetime, UTC
from uuid import uuid4


@dataclass
class Document:
    id: str
    title: str
    text: str
    created_at: datetime

    @staticmethod
    def create(title: str, text: str) -> "Document":
        if not title.strip():
            raise ValueError("Title cannot be empty")

        if not text.strip():
            raise ValueError("Text cannot be empty")

        return Document(
            id=str(uuid4()),
            title=title,
            text=text,
            created_at=datetime.now(UTC)
        )
