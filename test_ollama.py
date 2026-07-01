import ollama

response = ollama.chat(
    model="phi3:latest",
    messages=[
        {
            "role": "user",
            "content": "What is Retrieval-Augmented Generation (RAG)?"
        }
    ]
)

print(response["message"]["content"])