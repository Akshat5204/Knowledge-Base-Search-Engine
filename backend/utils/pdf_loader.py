# backend/utils/pdf_loader.py
from PyPDF2 import PdfReader
from io import BytesIO
from typing import Union


def extract_text_from_pdf(file_like: Union[bytes, "FileStorage", BytesIO]) -> str:
    """
    Extracts text from a PDF file-like object.

    `file_like` may be:
      - a Flask/Werkzeug FileStorage (request.files['file'])
      - a file-like object with .read() / .seek()
      - a bytes object containing the PDF

    Returns the concatenated text of all pages ('' if nothing extracted).
    """
    # Try a couple of ways to construct a PdfReader
    reader = None

    try:
        # If file_like is a FileStorage, PdfReader can accept it directly
        reader = PdfReader(file_like)
    except Exception:
        try:
            # Some file-likes require using their .stream or reading into BytesIO
            if hasattr(file_like, "stream"):
                file_like.stream.seek(0)
                reader = PdfReader(file_like.stream)
            else:
                # Read raw bytes and wrap in BytesIO
                file_like.seek(0)
                data = file_like.read()
                reader = PdfReader(BytesIO(data))
        except Exception as e:
            # Last resort: if file_like is raw bytes
            if isinstance(file_like, (bytes, bytearray)):
                reader = PdfReader(BytesIO(file_like))
            else:
                raise RuntimeError(f"Failed to read PDF: {e}")

    # Extract text safely
    pages_text = []
    for page in reader.pages:
        try:
            page_text = page.extract_text() or ""
        except Exception:
            page_text = ""
        pages_text.append(page_text)

    return "\n\n".join(pages_text)
