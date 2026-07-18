"""
Document styling utilities.
"""

from docx.document import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Inches, Pt


class DocumentStyleManager:
    """
    Applies consistent formatting
    to Microsoft Word documents.
    """

    def apply(
        self,
        document: Document,
    ) -> None:
        """
        Configure the document styles.
        """

        section = document.sections[0]

        section.top_margin = Inches(1)

        section.bottom_margin = Inches(1)

        section.left_margin = Inches(1)

        section.right_margin = Inches(1)

        normal = document.styles["Normal"]

        normal.font.name = "Calibri"

        normal.font.size = Pt(11)

        heading1 = document.styles["Heading 1"]

        heading1.font.name = "Calibri"

        heading1.font.size = Pt(18)

        heading1.font.bold = True

        heading2 = document.styles["Heading 2"]

        heading2.font.name = "Calibri"

        heading2.font.size = Pt(14)

        heading2.font.bold = True