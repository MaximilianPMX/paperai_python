# paperai/src/paperai/pdf_handler.py

from io import BytesIO
from typing import Optional, Tuple

from pypdf import PdfReader


def read_pdf(file_path: str) -> Tuple[Optional[str], Optional[dict]]:
    """Reads a PDF file and extracts the text and metadata.

    Args:
        file_path: The path to the PDF file.

    Returns:
        A tuple containing the text content of the PDF and metadata, or (None, None) if an error occurs.
    """
    try:
        with open(file_path, 'rb') as f:
            reader = PdfReader(f)
            text = "".join(page.extract_text() for page in reader.pages)
            metadata = reader.metadata
            return text, metadata
    except Exception as e:
        print(f"Error reading PDF {file_path}: {e}")
        return None, None


def read_pdf_from_bytes(file_bytes: bytes) -> Tuple[Optional[str], Optional[dict]]:
    """Reads a PDF from bytes and extracts the text and metadata.

    Args:
        file_bytes: The bytes of the PDF file.

    Returns:
        A tuple containing the text content of the PDF, metadata or (None, None) if an error occurs.
    """
    try:
        reader = PdfReader(BytesIO(file_bytes))
        text = "".join(page.extract_text() for page in reader.pages)
        metadata = reader.metadata
        return text, metadata
    except Exception as e:
        print(f"Error reading PDF from bytes: {e}")
        return None, None
