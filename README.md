ab.txtGROQ_API_KEY="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"



# AI Document Chatbot (RAG System)

## 🚀 Overview

This project is a Retrieval-Augmented Generation (RAG) based chatbot that answers questions from a given document.

## 🧠 Architecture

1. Document is split into chunks
2. Each chunk is converted into embeddings
3. Stored in a vector store
4. User query is embedded
5. Similar chunks are retrieved
6. LLM generates answer using retrieved context

## 🛠 Tech Stack

* Python
* Sentence Transformers (embeddings)
* Groq (LLM)
* Custom Vector Store

## 🔥 Features

* Semantic search (not keyword-based)
* Context-aware answering
* Strict prompt to avoid hallucination
* Modular architecture

## 📌 Example

User: What is AI?
AI: AI is a field of computer science...

## 🎯 Learnings

* Embeddings and similarity search
* Chunking strategies
* RAG pipeline design
* Prompt engineering
* System architecture for AI apps

