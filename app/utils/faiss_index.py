import faiss
import numpy as np
import os

FAISS_INDEX_PATH = "faiss.index"
DIMENSION = 512

if os.path.exists(FAISS_INDEX_PATH):
    index = faiss.read_index(FAISS_INDEX_PATH)
else:
    index = faiss.IndexFlatL2(DIMENSION)

def add_embedding(embedding: np.ndarray):
    index.add(embedding)
    save_index()

def search_embedding(query_embedding: np.ndarray, top_k: int = 1):
    distances, indices = index.search(query_embedding, top_k)
    return distances[0], indices[0]

def save_index():
    faiss.write_index(index, FAISS_INDEX_PATH)