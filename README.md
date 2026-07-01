
# 📘 RAG Assistant (PDF Chatbot using Ollama + FAISS)

A lightweight Retrieval-Augmented Generation (RAG) system that lets you chat with your PDF documents using local LLMs via **Ollama**, embeddings, and **FAISS vector search**.

---

## 🚀 Features

- 📄 Load and read PDF documents
- ✂️ Split text into intelligent chunks
- 🔗 Generate embeddings using Ollama (`nomic-embed-text`)
- 🧠 Store and search embeddings using FAISS
- 🔍 Retrieve most relevant document sections
- 🤖 Generate answers using local LLM (`phi3`)
- 💻 Fully offline after setup

---

## 🧠 Tech Stack

- Python 3.11+
- Ollama (phi3, nomic-embed-text)
- FAISS (Vector Database)
- PyPDF
- NumPy

---

## 📁 Project Structure
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
│ └── your_pdf.pdf
│
├── .gitignore
└── requirements.txt

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/anusha-coder21/Rag-assistent.git
cd Rag-assistent

2️⃣Create virtual environment (IMPORTANT)
py -3.11 -m venv venv311
venv311\Scripts\activate

3️⃣Install dependencies
pip install -r requirements.txt

4️⃣install Ollama

Download Ollama:
👉 https://ollama.com

Pull required models:

ollama pull phi3
ollama pull nomic-embed-text

Start Ollama:

ollama serve

▶️Run the Project
python main.py

💬 How It Works
PDF is loaded and cleaned
Text is split into chunks
Each chunk is converted into embeddings
FAISS stores embeddings in vector space
User question is converted into embedding
Similar chunks are retrieved
Context is sent to LLM (phi3)
Final answer is generated

Example

Input:

what is machine learning

Output:

Machine Learning is a branch of Artificial Intelligence that enables systems t

Important Notes
Python Version

Use:

Python 3.11 (NOT 3.13)

Ollama must be running
ollama serve
