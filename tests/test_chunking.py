
from src.chunking import split_text


def test_split_text_returns_chunks():
    text = "A" * 2000
    chunks = split_text(text, chunk_size=800, overlap=200)

    assert len(chunks) > 1
    assert all(len(chunk) <= 800 for chunk in chunks)


def test_split_text_empty_input():
    assert split_text("") == []
