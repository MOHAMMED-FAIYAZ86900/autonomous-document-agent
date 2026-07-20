from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """

    # ----------------------------------------------------
    # Application
    # ----------------------------------------------------

    app_name: str = Field(default="Autonomous Document Agent")
    app_version: str = Field(default="1.0.0")

    environment: str = Field(default="development")
    debug: bool = Field(default=True)

    log_level: str = Field(default="INFO")

    # ----------------------------------------------------
    # LLM Configuration
    # ----------------------------------------------------

    llm_provider: str = Field(default="groq")

    groq_api_key: str

    model_name: str = Field(
        default="llama-3.3-70b-versatile"
    )

    max_retries: int = Field(
        default=2,
        ge=0,
        le=5,
    )

    enable_reflection: bool = Field(default=True)

    # ----------------------------------------------------
    # Storage
    # ----------------------------------------------------

    output_dir: Path = Field(
        default=Path("storage/generated_docs")
    )

    # ----------------------------------------------------
    # Pydantic Settings
    # ----------------------------------------------------

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()