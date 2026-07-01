from embeddings import model

def retrieve(query, vector_store):

    query_embedding = model.encode([query])[0]

    return vector_store.search(query_embedding)