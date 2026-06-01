from rag.rag_service import RAGService

rag = RAGService()

result = rag.ingest_document(
    "sample.pdf"
)

print(result)

answer = rag.query(
    "What is this document about?"
)

print(answer)
