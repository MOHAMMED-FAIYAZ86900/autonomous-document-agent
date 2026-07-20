"""
Microsoft Word document generator.
"""

from app.agent.state import AgentState
from app.core.logging import get_logger
from app.document.builder import DocumentBuilder
from app.storage.manager import StorageManager


class DocumentGenerator:
    """
    Generates Microsoft Word documents from AI-generated content.
    """

    def __init__(self):
        self.logger = get_logger(__name__)
        self.storage = StorageManager()

    def generate(self, state: AgentState) -> AgentState:
        """
        Generate a DOCX file from generated content.
        """

        self.logger.info("Document generation started.")

        try:
            builder = DocumentBuilder()

            builder.add_title("AI Generated Document")

            builder.add_content(state.generated_content or "")

            document = builder.build()

            filename = "generated_document.docx"

            output_path = self.storage.save_document(
                document=document,
                filename=filename,
            )

            state.output_file = str(output_path)

            self.logger.info(
                "Document saved successfully: %s",
                output_path,
            )

            return state

        except Exception as exc:
            self.logger.exception("Document generation failed.")

            state.status = "failed"
            state.errors.append(str(exc))

            return state
