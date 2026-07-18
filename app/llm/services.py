"""
Service layer for interacting with Large Language Models.
"""

from app.core.logging import get_logger
from app.llm.base import LLMProvider
from app.llm.gemini import GeminiProvider
from app.llm.prompts import PromptManager
from app.llm.schemas import (
    LLMRequest,
    LLMResponse,
)


class LLMService:
    """
    High-level service for interacting with LLM providers.
    """

    def __init__(
        self,
        provider: LLMProvider | None = None,
    ) -> None:

        self.logger = get_logger(__name__)

        self.provider = provider or GeminiProvider()

    def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:

        self.logger.info(
            "Sending request to LLM provider."
        )

        return self.provider.generate(request)

    def generate_plan(
        self,
        user_request: str,
    ) -> LLMResponse:

        prompt = PromptManager.planner_prompt(
            user_request
        )

        request = LLMRequest(
            prompt=prompt
        )

        return self.generate(request)

    def generate_document(
        self,
        execution_plan: str,
    ) -> LLMResponse:

        prompt = PromptManager.document_prompt(
            execution_plan
        )

        request = LLMRequest(
            prompt=prompt
        )

        return self.generate(request)

    def review_document(
        self,
        document: str,
    ) -> LLMResponse:

        prompt = PromptManager.reflection_prompt(
            document
        )

        request = LLMRequest(
            prompt=prompt
        )

        return self.generate(request)