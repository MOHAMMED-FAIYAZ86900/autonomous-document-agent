"""
Gemini implementation of the LLM provider.
"""

from google import genai

from app.core.config import settings
from app.core.exceptions import LLMError
from app.core.logging import get_logger

from app.llm.base import LLMProvider
from app.llm.schemas import (
    LLMRequest,
    LLMResponse,
)


class GeminiProvider(LLMProvider):
    """
    Google Gemini implementation of the LLMProvider interface.
    """

    def __init__(self) -> None:
        self.logger = get_logger(__name__)

        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

        self.model_name = settings.model_name

    def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:
        """
        Generate a response using Gemini.
        """

        try:
            self.logger.info("Sending request to Gemini.")

            response = self.client.models.generate_content(
                model=self.model_name,
                contents=request.prompt,
            )

            if not response.text:
                raise LLMError(
                    "Gemini returned an empty response."
                )

            self.logger.info("Received response from Gemini.")

            return LLMResponse(
                content=response.text,
                model=self.model_name,
                success=True,
                finish_reason="STOP",
            )

        except Exception as exc:
            self.logger.exception(
                "Gemini request failed."
            )

            raise LLMError(
                f"Gemini generation failed: {exc}"
            ) from exc