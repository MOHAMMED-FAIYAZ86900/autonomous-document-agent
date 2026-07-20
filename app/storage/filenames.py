"""
Filename generation utilities.
"""

import re
from datetime import datetime
from uuid import uuid4


class FilenameGenerator:
    """
    Generates unique filenames
    for generated documents.
    """

    @staticmethod
    def sanitize(
        text: str,
    ) -> str:
        """
        Convert arbitrary text into
        a filesystem-safe filename.
        """

        text = text.lower().strip()

        text = re.sub(
            r"[^a-z0-9]+",
            "_",
            text,
        )

        return text.strip("_")

    @staticmethod
    def generate(
        document_type: str | None,
    ) -> str:
        """
        Generate a unique filename.
        """

        prefix = FilenameGenerator.sanitize(document_type or "document")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        unique = uuid4().hex[:6]

        return f"{prefix}_{timestamp}_{unique}.docx"
