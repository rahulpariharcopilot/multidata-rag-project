"""
Configuration management using Pydantic Settings.
Loads environment variables from .env file.
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application
    APP_NAME: str = "Multi-Source RAG + Text-to-SQL"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"

    # OpenAI Configuration
    OPENAI_API_KEY: str

    # Pinecone Configuration
    PINECONE_API_KEY: str
    PINECONE_ENVIRONMENT: str = "us-east-1-aws"
    PINECONE_INDEX_NAME: str = "rag-documents"

    # Supabase/PostgreSQL Configuration
    DATABASE_URL: str

    # OPIK Monitoring
    OPIK_API_KEY: Optional[str] = None

    # Text Chunking Configuration
    CHUNK_SIZE: int = 512
    CHUNK_OVERLAP: int = 50

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


# Global settings instance
settings = Settings()
