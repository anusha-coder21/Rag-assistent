from pdf_loader import load_pdf

text = load_pdf("data/BCS602-module-1-pdf (1).pdf")

print(text[:1000])