from fastapi import APIRouter, UploadFile
from rag.rag_service import RAGService
import shutil

router = APIRouter()

rag_service = RAGService()


@router.post("/upload")

async def upload_document(file: UploadFile):

    path = f"uploads/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = rag_service.ingest_document(path)

    return result


@router.get("/query")

async def query(question: str):

    result = rag_service.query(question)

    return result
