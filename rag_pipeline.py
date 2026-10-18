
from src.chunking import split_text
from src.retrieval import retrieve_relevant_chunk


def answer_question(document_text, question):
    """Retrieve the most relevant passage from a document."""
    if not document_text.strip():
        return "The document contains no readable text."

    if not question.strip():
        return "Please enter a question."

    chunks = split_text(document_text)

    result = retrieve_relevant_chunk(question, chunks)

    if result is None:
        return "No relevant passage could be retrieved."

    return result
