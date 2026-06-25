import json

from loaders.document_loader import load_document
from utils.chunker import create_chunks
from db.chroma_manager import vectordb
from utils.hash_utils import calculate_file_hash


def ingest_document(file_path):

    # Calculate file hash
    file_hash = calculate_file_hash(file_path)

    # Load existing hashes
    try:
        with open("indexed_files.json", "r") as f:
            indexed_hashes = json.load(f)
    except:
        indexed_hashes = []

    # Check if already indexed
    if file_hash in indexed_hashes:
        return {
            "message": "Document already indexed"
        }

    # Load document
    text = load_document(file_path)

    # Create chunks
    chunks = create_chunks(text)

    # Add metadata

    import os
    from datetime import datetime



    file_name = os.path.basename(file_path)

    file_size = os.path.getsize(file_path)

    uploaded_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for chunk in chunks:

        chunk.metadata = {
            "source": file_path,
            "file_name": file_name,
            "file_hash": file_hash,
            "file_size": file_size,
            "uploaded_at": uploaded_at
        }

        
    # Store in ChromaDB
    vectordb.add_documents(chunks)

    # Save hash
    indexed_hashes.append(file_hash)

    with open("indexed_files.json", "w") as f:
        json.dump(indexed_hashes, f, indent=4)

    return {
        "message": "Document indexed successfully",
        "chunks": len(chunks)
    }
