from pdf_loader import load_pdf
from chunker import chunk_text
from embeddings import create_embeddings
from vector_store import VectorStore
from retriever import Retriever
import ollama

# Load PDF
text = load_pdf("data/BCS602-module-1-pdf (1).pdf")

# Chunk
chunks = chunk_text(text)

# Embeddings for documents
embeddings = create_embeddings(chunks)

# Vector DB
store = VectorStore(embedding_dim=768)
store.add(embeddings, chunks)

# Retriever
retriever = Retriever(store, create_embeddings)

print("RAG READY 🚀")

while True:
    query = input("Ask: ")

    # 1. Get context
    context_chunks = retriever.get_relevant_chunks(query)

    context = "\n".join(
        [f"Chunk {i+1}:\n{chunk.strip()}" for i, chunk in enumerate(context_chunks)]
    )

    print("\n🔍 Retrieved Context:\n", context)

    # 2. Ask LLM
    response = ollama.chat(
    model="phi3:latest",
    messages=[
        {
            "role": "system",
            "content": """
You are an expert academic tutor.

Your job:
Convert the given context into CLEAN STUDY NOTES.

RULES:
- Do NOT repeat chunks
- Do NOT copy raw text
- Do NOT show "context"
- Always structure answers like exam notes
- Use headings and bullet points
- Keep meaning 100% accurate
- If multiple points exist, organize them logically
- If answer is missing, say: "Not found in document"
"""
        },
        {
            "role": "user",
            "content": f"""
Convert this into clean study notes.

Context:
{context}

Question:
{query}
"""
        }
    ]
)

    print("\n🧠 FINAL ANSWER:\n")
    print(response["message"]["content"].strip())
    print("\n" + "-"*50)
    print("\n" + "-"*50)