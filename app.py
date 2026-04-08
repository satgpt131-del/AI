from rag_system import smart_chunk_text, rag_pipeline
from vector_store import VectorStore

def load_document(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def main():

    print("📄 AI Document Chatbot\n")

    file_path = input("Enter document path (e.g., sample.txt): ")

    try:
        text = load_document(file_path)
    except:
        print("❌ Failed to load file")
        return

    # Step 1: Chunk
    chunks = smart_chunk_text(text)

    # Step 2: Store
    store = VectorStore()
    store.add_documents(chunks)

    print("\n✅ Document loaded successfully!")
    print("You can now ask questions.\n")

    while True:
        query = input("❓ Ask a question (or type 'exit'): ")

        if query.lower() == "exit":
            break

        answer = rag_pipeline(query, store)

        print("\n🤖 Answer:\n", answer)
        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    main()