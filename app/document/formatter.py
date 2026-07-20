"""
Document formatting utilities.
"""

from dataclasses import dataclass


@dataclass
class DocumentBlock:
    """
    Represents a logical block inside a document.
    """

    type: str
    content: str


class DocumentFormatter:
    """
    Converts raw AI-generated text into
    structured document blocks.
    """

    def format(
        self,
        content: str,
    ) -> list[DocumentBlock]:
        """
        Parse raw text into structured blocks.
        """

        blocks: list[DocumentBlock] = []

        for line in content.splitlines():

            line = line.strip()

            if not line:
                continue

            if len(line) < 60 and not line.endswith("."):

                blocks.append(
                    DocumentBlock(
                        type="heading",
                        content=line,
                    )
                )

            else:

                blocks.append(
                    DocumentBlock(
                        type="paragraph",
                        content=line,
                    )
                )

        return blocks
