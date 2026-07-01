from pdf_loader import load_pdf
from chunker import chunk_text

text = load_pdf("data/BCS602-module-1-pdf (1).pdf")

chunks = chunk_text(text)

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])

print("\nSecond Chunk:\n")
print(chunks[1])