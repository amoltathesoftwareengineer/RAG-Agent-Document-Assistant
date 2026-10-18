
def split_text(text, chunk_size=800, overlap=200):
    """Split document text into overlapping chunks."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be between 0 and chunk_size")

    chunks = []
    start = 0

    while start < len(text):
        chunk = text[start:start + chunk_size]

        if chunk.strip():
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks
