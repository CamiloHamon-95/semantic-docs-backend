from domain.models.document import Document


class CreateDocumentUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, title: str, text: str) -> Document:
        document = Document.create(title=title, text=text)
        self.repository.save(document)
        return document
