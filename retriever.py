class Retriever:
    def __init__(self, vector_store, embed_fn):
        self.store = vector_store
        self.embed_fn = embed_fn

    def get_relevant_chunks(self, query, top_k=3):
        query_embedding = self.embed_fn([query])[0]
        results = self.store.search(query_embedding, top_k)
        return results