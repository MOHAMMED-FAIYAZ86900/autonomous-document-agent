"""
Storage management utilities.
"""

from pathlib import Path

from docx.document import Document

from app.core.config import settings
from app.core.logging import get_logger


class StorageManager:
    """
    Handles all document storage operations.
    """

    def __init__(self) -> None:
        self.logger = get_logger(__name__)

        self.storage_path = (
            settings.STORAGE_DIR
            / "generated_docs"
        )

        self.storage_path.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save_document(
        self,
        document: Document,
        filename: str,
    ) -> Path:
        """
        Save a DOCX document.
        """

        output_path = (
            self.storage_path / filename
        )

        document.save(output_path)

        self.logger.info(
            "Document saved: %s",
            output_path,
        )

        return output_path

    def exists(
        self,
        filename: str,
    ) -> bool:
        """
        Check whether a document exists.
        """

        return (
            self.storage_path / filename
        ).exists()

    def get_path(
        self,
        filename: str,
    ) -> Path:
        """
        Return absolute path
        of a stored document.
        """

        return (
            self.storage_path / filename
        )

    def list_documents(
        self,
    ) -> list[Path]:
        """
        Return all generated DOCX files.
        """

        return sorted(
            self.storage_path.glob("*.docx")
        )