# paperai/src/paperai/data_loader.py

import os
from typing import Optional, Tuple

from paperai.pdf_handler import read_pdf


def load_document(file_path: str) -> Tuple[Optional[str], Optional[dict]]:
    """Loads a document from the given file path.

    Args:
        file_path: The path to the document file.

    Returns:
        A tuple containing the text content of the document and its metadata.
        Returns (None, None) if the file cannot be read or is not supported.
    """
    _, file_extension = os.path.splitext(file_path)

    if file_extension.lower() == ".pdf":
        return read_pdf(file_path)
    elif file_extension.lower() == ".txt":
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
                return text, {}
        except Exception as e:
            print(f"Error reading TXT file {file_path}: {e}")
            return None, None
    else:
        print(f"Unsupported file type: {file_extension}")
        return None, None
