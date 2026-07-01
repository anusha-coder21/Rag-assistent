📘 RAG Assistant (PDF Chatbot using Ollama + FAISS)

A simple Retrieval-Augmented Generation (RAG) system that allows users to upload a PDF and ask questions from it using local LLMs via Ollama, embeddings, and FAISS vector search.

🚀 Features
Load PDF documents
Split text into chunks
Convert chunks into embeddings using Ollama (nomic-embed-text)
Store embeddings in FAISS vector database
Retrieve relevant chunks using semantic search
Generate answers using phi3 (local LLM via Ollama)
🧠 Tech Stack
Python 3.11+
Ollama (phi3 + nomic-embed-text)
FAISS (vector database)
PyPDF
NumPy
📁 Project Structure
Rag-Assistent/
│
├── main.py
├── pdf_loader.py
├── chunker.py
├── embeddings.py
├── vector_store.py
├── retriever.py
├── test_embed.py
├── data/
│   └── your_pdf.pdf
│
├── .gitignore
└── requirements.txt
⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/anusha-coder21/Rag-assistent.git
cd Rag-assistent
2. Create virtual environment (IMPORTANT)
py -3.11 -m venv venv311
venv311\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Install & setup Ollama

Download Ollama:
👉 https://ollama.com

Then pull required models:

ollama pull phi3
ollama pull nomic-embed-text
▶️ Run the Project
python main.py
💬 How it works
PDF is loaded
Text is split into chunks
Each chunk is converted into embeddings
FAISS stores embeddings
User question → embedding → similarity search
Top chunks are sent to LLM (phi3)
Final answer is generated
📌 Example
Ask: what is machine learning

Answer:
Machine Learning is a branch of AI that enables systems to learn from data without being explicitly programmed...
❗ Important Notes
1. Python version

Use:

Python 3.11 (NOT 3.13)
2. Ollama must be running

Before running project:

ollama serve
3. Ignore these files in Git

Make sure .gitignore contains:

venv/
venv311/
__pycache__/
*.pyc
.env
🧠 Future Improvements
Add Streamlit UI
Support multiple PDFs
Chat memory
Better chunking strategy
Cloud deployment
