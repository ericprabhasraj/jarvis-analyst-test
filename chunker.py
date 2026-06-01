from langchain.text_splitter import RecursiveCharacterTextSplitter

class DocumentChunker:

    @staticmethod
    def split(documents):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            length_function=len
        )

        chunks = splitter.split_documents(documents)

        return chunks
