"""
Groq implementation of the LLM provider.
"""

from groq import Groq

from app.core.config import settings
from app.core.exceptions import LLMError
from app.core.logging import get_logger
from app.llm.base import LLMProvider
from app.llm.schemas import LLMRequest, LLMResponse


class GroqProvider(LLMProvider):
    """
    Groq implementation of the LLMProvider interface.
    """

    def __init__(self):
        self.logger = get_logger(__name__)
        self.model_name = settings.model_name
        self.client = None

        self.logger.info("Groq provider initialized (lazy client creation).")

    def _get_client(self):
        """
        Lazily create the Groq client only when required.
        """

        if self.client is None:

            if not settings.groq_api_key:
                raise LLMError("GROQ_API_KEY is not configured.")

            self.client = Groq(api_key=settings.groq_api_key)

        return self.client

    def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:

        try:

            client = self._get_client()

            messages = []

            if request.system_prompt:
                messages.append(
                    {
                        "role": "system",
                        "content": request.system_prompt,
                    }
                )

            messages.append(
                {
                    "role": "user",
                    "content": request.prompt,
                }
            )

            response = client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=request.temperature,
                max_tokens=request.max_tokens,
            )

            content = response.choices[0].message.content

            if not content:
                raise LLMError("Groq returned an empty response.")

            return LLMResponse(
                content=content,
                model=self.model_name,
                success=True,
                finish_reason=response.choices[0].finish_reason,
            )

        except Exception as exc:

            self.logger.exception("Groq request failed.")

            raise LLMError(f"Groq generation failed: {exc}") from exc
