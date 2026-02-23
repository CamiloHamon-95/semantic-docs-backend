import sqlite3
from domain.models.document import Document


class SQLiteDocumentRepository:
    def __init__(self, db_path: str = "documents.db"):
        self.connection = sqlite3.connect(
            db_path, check_same_thread=False
        )
        self._create_table()

    def _create_table(self):
        self.connection.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            text TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """)
        self.connection.commit()

    def save(self, document: Document):
        command = (
            "INSERT INTO documents "
            "(id, title, text, created_at) VALUES (?, ?, ?, ?)"
        )
        self.connection.execute(
            command,
            (
                document.id,
                document.title,
                document.text,
                document.created_at.isoformat()
            )
        )
        self.connection.commit()
