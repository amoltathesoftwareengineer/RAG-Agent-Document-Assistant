
from sklearn.feature_extraction.text import TfidfVectorizer


def create_embeddings(texts):
    """Convert text chunks into TF-IDF numerical vectors."""
    if not texts:
        return None, None

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)

    return vectorizer, vectors
