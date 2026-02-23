from fastapi import FastAPI
from pydantic import BaseModel

from application.use_cases.create_document import CreateDocumentUseCase
from infrastructure.db.sqlite_repository import SQLiteDocumentRepository


app = FastAPI()
repository = SQLiteDocumentRepository()
use_case = CreateDocumentUseCase(repository)


class CreateDocumentRequest(BaseModel):
    title: str
    text: str


@app.post("/documents")
def create_document(request: CreateDocumentRequest):
    document = use_case.execute(request.title, request.text)
    return {
        "id": document.id,
        "title": document.title,
        "created_at": document.created_at
    }