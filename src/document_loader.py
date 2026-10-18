
from pypdf import PdfReader


def load_pdf(uploaded_file):
    """Extract readable text from an uploaded PDF."""
    reader = PdfReader(uploaded_file)
    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if text.strip():
            pages.append({
                "page": page_number,
                "text": text
            })

    return pages
