
import streamlit as st

from src.document_loader import load_pdf
from src.rag_pipeline import answer_question

st.set_page_config(
    page_title="RAG Agent Document Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 RAG Agent Document Assistant")
st.write("Upload a PDF and ask questions about its content.")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file:
    try:
        pages = load_pdf(uploaded_file)
        document_text = "\n".join(page["text"] for page in pages)

        if document_text.strip():
            st.success(f"PDF loaded: {len(pages)} pages")

            question = st.text_input("Ask a question about your document")

            if question:
                result = answer_question(document_text, question)
                st.subheader("Relevant Context")
                st.write(result)
                st.caption(
                    "This shows retrieved document text, not an AI-generated answer."
                )
        else:
            st.warning("No readable text found in this PDF.")

    except Exception as error:
        st.error(f"Could not process the PDF: {error}")
