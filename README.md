# RAG for Codebases Project

## Project Overview
This project aims to build a Retrieval-Augmented Generation (RAG) system for exploring and querying large codebases. The system will index two different codebases and implement a question-answering system that retrieves relevant code snippets to assist a language model in generating informed answers.

### Codebases to be used:
1. **xv6-riscv** - A teaching operating system in C.
2. **llama_index** - The LlamaIndex project’s own code, in Python.

## Project Objectives
1. Implement a baseline RAG using LlamaIndex and ChromaDB.
2. Experiment with various chunking strategies and metadata to improve retrieval performance.
3. Evaluate the RAG system using relevant queries.

## Tasks Breakdown
- **CoderAgent:** Implement the coding functionality to index both codebases using specified chunking strategies and store in ChromaDB.
- **DocumenterAgent:** Document the process, methodologies, results, and analyses in a structured format.
- **PresenterAgent:** Create a presentation summarizing the project, methodologies, and outcomes.
- **VoiceOverAgent:** Develop voice-over scripts corresponding to the presentation slides.