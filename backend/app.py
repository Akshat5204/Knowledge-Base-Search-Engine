import os
from flask import Flask, request, jsonify
from flask_cors import CORS

# Import helper functions
from utils.pdf_loader import extract_text_from_pdf
from utils.text_splitter import split_text
from utils.embeddings import create_embeddings, search_similar
from rag_pipeline import generate_answer

from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
CORS(app)

# In-memory storage for uploaded text chunks
DOCUMENT_CHUNKS = []


@app.route("/upload", methods=["POST"])
def upload_file():
    """
    Upload a PDF file, extract text, split into chunks, create embeddings,
    and store the chunks in memory.
    """
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file provided"}), 400

    try:
        text = extract_text_from_pdf(file)
        chunks = split_text(text)
        if not chunks:
            return jsonify({"error": "No text extracted from PDF"}), 400

        create_embeddings(chunks)
        DOCUMENT_CHUNKS.extend(chunks)

        return jsonify({
            "message": "File uploaded and processed!",
            "chunks_count": len(chunks)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/query", methods=["POST"])
def query():
    data = request.get_json() or {}
    question = data.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        top_chunks = search_similar(question, k=4)
        answer = generate_answer(question, top_chunks)
        return jsonify({"answer": answer, "sources": top_chunks})
    except Exception as e:
        import traceback
        print("\n" + "="*80)
        print("❌ ERROR in /query endpoint:")
        print(traceback.format_exc())
        print("="*80 + "\n")
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
