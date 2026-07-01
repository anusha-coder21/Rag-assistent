import ollama

res = ollama.embeddings(
    model="nomic-embed-text",
    prompt="Retrieval-Augmented Generation is a method that combines search and LLMs"
)

print("Embedding length:", len(res["embedding"]))
print("First 10 values:", res["embedding"][:10])
