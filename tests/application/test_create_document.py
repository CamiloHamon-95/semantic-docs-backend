from application.use_cases.create_document import CreateDocumentUseCase


class FakeRepository:
    def __init__(self):
        self.saved = None

    def save(self, document):
        self.saved = document


def test_create_document_use_case():
    repo = FakeRepository()
    use_case = CreateDocumentUseCase(repo)

    document = use_case.execute("Title", "Text")

    assert repo.saved is not None
    assert document.title == "Title"
