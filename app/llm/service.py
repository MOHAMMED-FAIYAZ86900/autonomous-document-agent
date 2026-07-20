"""
LLM service layer.

Acts as a wrapper around the selected LLM provider.
"""

from app.core.config import settings
from app.core.logging import get_logger

from app.llm.groq import GroqProvider

from app.llm.schemas import (
    LLMRequest,
    LLMResponse,
)


class LLMService:
    """
    Wrapper around the configured LLM provider.
    """

    def __init__(self):

        self.logger = get_logger(__name__)

        provider = settings.llm_provider.lower()

        if provider == "groq":

            self.provider = GroqProvider()

        else:

            raise ValueError(
                f"Unsupported LLM Provider: {provider}"
            )

    def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:

        self.logger.info(
            "Sending request to %s provider.",
            settings.llm_provider.upper(),
        )

        return self.provider.generate(request)

    def generate_plan(
        self,
        prompt: str,
    ) -> LLMResponse:

        request = LLMRequest(
            prompt=prompt,
        )

        return self.generate(request)

    def generate_document(
        self,
        prompt: str,
    ) -> LLMResponse:

        request = LLMRequest(
            prompt=prompt,
        )

        return self.generate(request)

    def reflect(
        self,
        prompt: str,
    ) -> LLMResponse:

        request = LLMRequest(
            prompt=prompt,
        )

        return self.generate(request)