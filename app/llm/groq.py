"""
Groq implementation of the LLM provider.
"""

from groq import Groq

from app.core.config import settings
from app.core.exceptions import LLMError
from app.core.logging import get_logger

from app.llm.base import LLMProvider
from app.llm.schemas import (
    LLMRequest,
    LLMResponse,
)


class GroqProvider(LLMProvider):
    """
    Groq implementation of the LLMProvider interface.
    """

    def __init__(self):

        self.logger = get_logger(__name__)

        self.client = Groq(
            api_key=settings.groq_api_key
        )

        self.model_name = settings.model_name

        self.logger.info(
            f"Using Groq model: {self.model_name}"
        )

    def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:

        try:

            self.logger.info(
                "Sending request to Groq."
            )

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

            response = self.client.chat.completions.create(

                model=self.model_name,

                messages=messages,

                temperature=request.temperature,

                max_tokens=request.max_tokens,

            )

            content = response.choices[0].message.content

            if not content:

                raise LLMError(
                    "Groq returned an empty response."
                )

            self.logger.info(
                "Received response from Groq."
            )

            return LLMResponse(

                content=content,

                model=self.model_name,

                success=True,

                finish_reason=response.choices[0].finish_reason,

            )

        except Exception as exc:

            self.logger.exception(
                "Groq request failed."
            )

            raise LLMError(
                f"Groq generation failed: {exc}"
            ) from exc