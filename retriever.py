class Retriever:

    @staticmethod
    def search(query, vector_db, k=5):

        docs = vector_db.similarity_search(
            query=query,
            k=k
        )

        return docs
