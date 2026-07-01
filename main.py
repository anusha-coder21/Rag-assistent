from pdf_loader import load_pdf
from chunker import chunk_text
from embeddings import create_embeddings
from vector_store import VectorStore
from retriever import Retriever
import ollama

# Load PDF
text = load_pdf("data/BCS602-module-1-pdf (1).pdf")

# CLEAN TEXT (ADD HERE)
import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = text.replace("", "-")
    text = text.replace("‐", "-")
    return text.strip()

text = clean_text(text)

# THEN CHUNK
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
    chunk.replace("\n", " ").strip() for chunk in context_chunks
    )

    print("\n🔍 Retrieved Context:\n", context)

    # 2. Ask LLM
    response = ollama.chat(
    model="phi3:latest",
    messages=[
        {
            "role": "system",
            "content": """
You are an academic assistant.

TASK:
Convert context into clean exam notes.

STRICT RULES:
- Do NOT copy text exactly
- Do NOT hallucinate new words
- Do NOT repeat phrases
- Remove broken words or artifacts
- Fix grammar automatically
- Output must be clean Markdown notes

FORMAT:
# Title
## Definition
## Explanation
## Key Points
## Summary

If information is unclear, simplify it instead of copying noise.
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