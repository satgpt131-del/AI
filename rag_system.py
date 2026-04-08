from llmclient import call_llm
import re


def smart_chunk_text(text, chunk_size=200, overlap=50):
    sentences = re.split(r'(?<=[.!?]) +', text)

    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in sentences:
        words = sentence.split()
        length = len(words)

        if current_length + length > chunk_size:
            chunks.append(" ".join(current_chunk))

            overlap_words = current_chunk[-overlap:] if overlap < len(current_chunk) else current_chunk
            current_chunk = overlap_words + words
            current_length = len(current_chunk)
        else:
            current_chunk.extend(words)
            current_length += length

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def build_prompt(query, retrieved_chunks):
    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are a strict AI assistant.

Rules:
- Answer ONLY using the provided context.
- Do NOT use outside knowledge.
- If the answer is not clearly in the context, say "I don't know."
- Keep the answer concise.

Context:
{context}

Question:
{query}
"""
    return prompt

def rag_pipeline(query, store):

    results = store.search(query)

    # Edge case: no relevant chunks
    if not results:
        return "I don't know"

    print("\n--- Retrieved Chunks ---\n")
    for i, (doc, score) in enumerate(results):
        print(f"[{i+1}] Score: {score:.4f}")
        print(doc)
        print()

    # Extract only text
    top_chunks = [doc for doc, _ in results]

    prompt = build_prompt(query, top_chunks)

    messages = [
        {"role": "system", "content": "You are a strict AI assistant."},
        {"role": "user", "content": prompt}
    ]

    return call_llm(messages)