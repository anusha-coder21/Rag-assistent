import os

from dotenv import load_dotenv
import google.generativeai as genai

from pdf_loader import load_pdf
from chunker import chunk_text
from embeddings import create_embeddings
from vector_store import VectorStore
from retriever import retrieve

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

llm = genai.GenerativeModel("gemini-2.5-flash")

text = load_pdf("data/sample.pdf")

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

store = VectorStore(len(embeddings[0]))

store.add(embeddings, chunks)

while True:

    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        break

    context = retrieve(question, store)

    prompt = f"""
Answer ONLY from the context.

Context:
{' '.join(context)}

Question:
{question}
"""

    response = llm.generate_content(prompt)

    print("\nAnswer:\n")
    print(response.text)