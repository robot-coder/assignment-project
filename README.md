# Retrieval-Augmented Generation for Codebases

## Project Overview
This project aims to build a Retrieval-Augmented Generation (RAG) system that allows for exploration and querying of large codebases. It utilizes LlamaIndex for indexing and ChromaDB for vector storage, creating a pipeline to retrieve relevant code snippets for answering questions effectively. The codebases utilized are xv6-riscv (in C) and llama_index (in Python).

## Objectives
- Implement a baseline RAG system that adequately indexes codebases and allows for meaningful queries.
- Experiment with different chunking strategies and metadata to optimize retrieval.

## Setup Instructions
1. Clone the repository.
2. Install required packages using `pip install -r requirements.txt`.
3. Set up API keys for any external services (if necessary).
4. Run the indexing script to process the codebases.
5. Use the querying script to ask questions about the indexed data.

## Methodologies
- **Indexing**: Utilized LlamaIndex CodeSplitter to segment code into meaningful chunks while generating embeddings stored in ChromaDB.
- **Querying**: Integrated a querying mechanism that employs an LLM to answer questions by leveraging the retrieved code snippets.

## Results
- Metrics such as Precision@K and Recall will be documented in the comparative analysis.
- Insights from various chunking and augmentation strategies are summarized.

## Test Queries
- A comprehensive list of test queries utilized for evaluation will be provided.

## Acknowledgments
- A special mention to relevant resources and documentations that guided the development of this project.

## License
This project is licensed under the MIT License.