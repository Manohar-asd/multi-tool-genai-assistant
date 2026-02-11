import os
import faiss
import numpy as np
from pypdf import PdfReader
from openai_client import client, MODEL, EMBEDDING_MODEL
from dotenv import load_dotenv

load_dotenv()

VECTOR_DIM = 1536   # OpenAI embeddings dimension
INDEX_PATH = "vector.index"
TEXT_PATH = "chunks.txt"

def load_documents(folder="data/docs"):
    texts = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if file.endswith(".pdf"):
            reader = PdfReader(path)
            for page in reader.pages:
                texts.append(page.extract_text())
        elif file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                texts.append(f.read())

    return texts

def get_embedding(text: str):
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )
    return np.array(response.data[0].embedding, dtype="float32")

def build_index():
    texts = load_documents()
    index = faiss.IndexFlatL2(VECTOR_DIM)
    embeddings = []

    for text in texts:
        emb = get_embedding(text)
        embeddings.append(emb)

    embeddings = np.vstack(embeddings)
    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)

    with open(TEXT_PATH, "w", encoding="utf-8") as f:
        for text in texts:
            f.write(text.replace("\n", " ") + "\n")

    print("✅ Document index created")

if __name__ == "__main__":
    build_index()
