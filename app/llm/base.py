"""
Base interface for all Large Language Model providers.
"""

from abc import ABC, abstractmethod

from app.llm.schemas import LLMRequest, LLMResponse


class LLMProvider(ABC):
    """
    Abstract base class for all LLM providers.

    Every provider (Gemini, OpenAI, Claude, etc.)
    must implement this interface.
    """

    @abstractmethod
    def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:
        ...
        """
        Generate a response from the language model.

        Args:
            prompt: Input prompt sent to the model.

        Returns:
            The generated text response.

        Raises:
            LLMError: If generation fails.
        """
        raise NotImplementedError
