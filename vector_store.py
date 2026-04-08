from sentence_transformers import SentenceTransformer
import numpy as np


class VectorStore:

    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.documents = []
        self.embeddings = []

    def add_documents(self, docs):
        for doc in docs:
            emb = self.model.encode(doc)
            self.documents.append(doc)
            self.embeddings.append(emb)

    def cosine_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def search(self, query, top_k=5, min_score=0.3):
        query_emb = self.model.encode(query)

        scores = []

        for doc, emb in zip(self.documents, self.embeddings):
            score = self.cosine_similarity(query_emb, emb)

            if score >= min_score:
                scores.append((doc, score))

        scores.sort(key=lambda x: x[1], reverse=True)

        return scores[:top_k]