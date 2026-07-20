"""
Document download endpoints.
"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from app.schemas.api import DocumentInfo
from app.storage.manager import StorageManager

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

storage = StorageManager()


@router.get(
    "",
    response_model=list[DocumentInfo],
)
def list_documents() -> list[DocumentInfo]:

    documents = storage.list_documents()

    return [
        DocumentInfo(
            filename=document.name,
            size=document.stat().st_size,
        )
        for document in documents
    ]


@router.get(
    "/{filename}",
)
def download_document(
    filename: str,
):

    if not storage.exists(filename):

        raise HTTPException(
            status_code=404,
            detail="Document not found.",
        )

    path = storage.get_path(filename)

    return FileResponse(
        path,
        filename=filename,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
