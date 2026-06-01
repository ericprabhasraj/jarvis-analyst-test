from langchain_community.vectorstores import FAISS

class VectorStore:

    @staticmethod
    def create(chunks, embeddings):

        db = FAISS.from_documents(
            chunks,
            embeddings
        )

        return db

    @staticmethod
    def save(db, path="vector_db"):

        db.save_local(path)

    @staticmethod
    def load(embeddings, path="vector_db"):

        return FAISS.load_local(
            path,
            embeddings,
            allow_dangerous_deserialization=True
        )
