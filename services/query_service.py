from db.chroma_manager import vectordb
from llm.groq_llm import llm


def ask_question(question):

    # Retrieve top 3 relevant chunks
    results = vectordb.similarity_search(
        question,
        k=3
    )

    # Build context for the LLM
    context = "\n".join(
        [doc.page_content for doc in results]
    )

    prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}
"""

    # Generate answer
    response = llm.invoke(prompt)

    # Collect document metadata
    documents = []

    for doc in results:

        documents.append({
            "file_name": doc.metadata.get("file_name"),
            "uploaded_at": doc.metadata.get("uploaded_at"),
            "source": doc.metadata.get("source"),
            "file_size": doc.metadata.get("file_size")
        })

    # Return answer and metadata
    return {
        "answer": response.content,
        "documents": documents
    }
