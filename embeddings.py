import ollama

def create_embeddings(texts):
    embeddings = []

    for text in texts:
        res = ollama.embeddings(
            model="nomic-embed-text",
            prompt=text
        )
        embeddings.append(res["embedding"])

    return embeddings