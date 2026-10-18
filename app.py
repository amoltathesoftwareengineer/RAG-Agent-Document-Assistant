
import streamlit as st
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="RAG Agent Document Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 RAG Agent Document Assistant")
st.write("Upload a PDF and ask questions about its content.")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file:
    reader = PdfReader(uploaded_file)
    pages = [page.extract_text() or "" for page in reader.pages]
    text = "\n".join(pages)

    chunks = [
        text[i:i + 800]
        for i in range(0, len(text), 600)
        if text[i:i + 800].strip()
    ]

    st.success(f"PDF loaded successfully: {len(pages)} pages")

    question = st.text_input("Ask a question about your document")

    if question and chunks:
        vectorizer = TfidfVectorizer()
        matrix = vectorizer.fit_transform(chunks + [question])
        scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()
        best_index = scores.argmax()

        st.subheader("Retrieved Context")
        st.write(chunks[best_index])

        st.caption(
            "This is a relevant text passage, not an AI-generated answer."
        )

    elif question and not chunks:
        st.warning("No readable text found in this PDF.")
