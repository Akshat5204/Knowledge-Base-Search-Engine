# backend/utils/text_splitter.py

def split_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> list:
    """
    Split a long text into overlapping chunks.

    :param text: The input text to split.
    :param chunk_size: Maximum characters per chunk.
    :param overlap: Number of characters each chunk should overlap with the previous chunk.
    :return: List of text chunks (may be empty if text is falsy).
    """
    if not text:
        return []

    if chunk_size <= 0:
        raise ValueError("chunk_size must be > 0")
    if overlap < 0:
        raise ValueError("overlap must be >= 0")
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    start = 0
    length = len(text)
    step = chunk_size - overlap

    while start < length:
        end = min(start + chunk_size, length)
        chunks.append(text[start:end])
        start += step

    return chunks
