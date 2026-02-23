import pytest
from domain.models.document import Document


def test_create_document_success():
    doc = Document.create("Title", "Text")
    assert doc.title == "Title"


def test_create_document_empty_title():
    with pytest.raises(ValueError):
        Document.create("", "Text")
