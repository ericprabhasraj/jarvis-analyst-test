from rag.loader import DocumentLoader
from rag.chunker import DocumentChunker
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore
from rag.retriever import Retriever


class RAGService:

    def __init__(self):

        self.embeddings = EmbeddingModel.load()
        self.vector_db = None

    def ingest_document(self, pdf_path):

        docs = DocumentLoader.load_pdf(pdf_path)

        chunks = DocumentChunker.split(docs)

        self.vector_db = VectorStore.create(
            chunks,
            self.embeddings
        )

        VectorStore.save(self.vector_db)

        return {
            "status": "success",
            "chunks": len(chunks)
        }

    def query(self, question):

        docs = Retriever.search(
            question,
            self.vector_db
        )

        context = "\n".join(
            [doc.page_content for doc in docs]
        )

        return {
            "question": question,
            "context": context,
            "sources": len(docs)
        }
