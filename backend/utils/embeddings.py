from langchain_community.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

import os

# Simple global (in-memory) vector store for demo use
_vector_store = None
_embeddings = None


def _get_embeddings():
    """
    Returns a global embedding model instance.
    Requires OPENAI_API_KEY in the environment.
    """
    global _embeddings
    if _embeddings is None:
        try:
            _embeddings = OpenAIEmbeddings()
        except Exception as e:
            raise RuntimeError(
                f"Failed to initialize OpenAIEmbeddings. Ensure OPENAI_API_KEY is set. Details: {e}"
            )
    return _embeddings


def create_embeddings(chunks):
    """
    Takes a list of text chunks, computes embeddings, and stores them in FAISS vector store.
    """
    global _vector_store
    if not chunks:
        print("⚠️ No chunks provided for embedding.")
        return

    try:
        emb = _get_embeddings()
        _vector_store = FAISS.from_texts(chunks, embedding=emb)
        print(f"✅ Created FAISS vector store with {len(chunks)} chunks.")
    except Exception as e:
        print(f"❌ Error creating embeddings: {e}")


def search_similar(query, k=3):
    """
    Searches for the top-k most similar chunks to the query.
    Returns a list of chunk texts.
    """
    global _vector_store
    if _vector_store is None:
        print("⚠️ No vector store found. Upload and process documents first.")
        return []

    try:
        results = _vector_store.similarity_search(query, k=k)
        return [getattr(r, "page_content", str(r)) for r in results]
    except Exception as e:
        print(f"❌ Error during similarity search: {e}")
        return []
