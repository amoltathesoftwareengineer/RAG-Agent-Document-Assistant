
from sklearn.metrics.pairwise import cosine_similarity

from src.embeddings import create_embeddings


def retrieve_relevant_chunk(question, chunks):
    """Return the text chunk most relevant to a question."""
    if not chunks or not question.strip():
        return None

    vectorizer, vectors = create_embeddings(chunks + [question])

    question_vector = vectors[-1]
    chunk_vectors = vectors[:-1]

    scores = cosine_similarity(question_vector, chunk_vectors).flatten()
    best_index = scores.argmax()

    return chunks[best_index]
