import os
import faiss
import numpy as np
from azure_client import client, DEPLOYMENT

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "vector.index")
TEXT_PATH = os.path.join(BASE_DIR, "chunks.txt")
EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")

index = faiss.read_index(INDEX_PATH)

with open(TEXT_PATH, "r", encoding="utf-8") as f:
    documents = f.readlines()

def get_embedding(text: str):
    response = client.embeddings.create(
        model=EMBEDDING_DEPLOYMENT,
        input=text
    )
    return np.array(response.data[0].embedding, dtype="float32")

def document_qa(question: str) -> str:
    q_emb = get_embedding(question).reshape(1, -1)
    _, indices = index.search(q_emb, k=3)

    context = " ".join([documents[i] for i in indices[0]])

    response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[
            {"role": "system", "content": "Answer only using the provided document context."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
        ]
    )

    return response.choices[0].message.content
