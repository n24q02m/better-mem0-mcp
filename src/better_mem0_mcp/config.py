"""
better-mem0-mcp: Zero-setup MCP Server for AI memory.

Configuration via environment variables:
- DATABASE_URL: PostgreSQL connection string
- API_KEYS: Provider:key pairs (e.g., "gemini:AIza...,openai:sk-xxx")
- LLM_MODELS: Model fallback chain (e.g., "gemini/gemini-3-flash-preview,openai/gpt-4o-mini")
- EMBEDDER_MODELS: Embedding fallback chain
"""

import os
from functools import lru_cache
from urllib.parse import parse_qs, urlparse

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuration with multi-key and fallback support."""

    model_config = ConfigDict(extra="ignore")

    # Database (Required)
    database_url: str = ""

    # API Keys: "provider:key,provider:key,..."
    api_keys: str = ""

    # Models with fallback: "provider/model,provider/model,..."
    # Note: For >2000 dims, HNSW index is disabled (uses exact search)
    llm_models: str = "gemini/gemini-3-flash-preview"
    embedder_models: str = "gemini/gemini-embedding-001"

    def setup_api_keys(self) -> dict[str, list[str]]:
        """
        Parse API_KEYS and set environment variables for LiteLLM.

        Returns:
            Dict mapping provider to list of API keys.
        """
        env_map = {
            "gemini": "GOOGLE_API_KEY",
            "openai": "OPENAI_API_KEY",
            "anthropic": "ANTHROPIC_API_KEY",
            "groq": "GROQ_API_KEY",
            "deepseek": "DEEPSEEK_API_KEY",
            "mistral": "MISTRAL_API_KEY",
        }

        keys_by_provider: dict[str, list[str]] = {}

        for pair in self.api_keys.split(","):
            pair = pair.strip()
            if ":" not in pair:
                continue

            provider, key = pair.split(":", 1)
            provider = provider.strip().lower()
            key = key.strip()

            if not key:
                continue

            keys_by_provider.setdefault(provider, []).append(key)

        # Set first key of each provider as env var (LiteLLM reads from env)
        for provider, keys in keys_by_provider.items():
            if provider in env_map and keys:
                os.environ[env_map[provider]] = keys[0]

        return keys_by_provider

    def parse_database_url(self) -> dict:
        """Parse DATABASE_URL into connection parameters."""
        if not self.database_url:
            return {}

        parsed = urlparse(self.database_url)
        query = parse_qs(parsed.query)

        return {
            "dbname": parsed.path[1:] if parsed.path else "mem0",
            "user": parsed.username or "postgres",
            "password": parsed.password or "",
            "host": parsed.hostname or "localhost",
            "port": parsed.port or 5432,
            "sslmode": query.get("sslmode", ["prefer"])[0],
        }

    def get_llm_config(self) -> dict:
        """Build Mem0 LLM configuration with fallback."""
        models = [m.strip() for m in self.llm_models.split(",") if m.strip()]

        if not models:
            models = ["gemini/gemini-3-flash-preview"]

        primary = models[0]
        fallbacks = models[1:] if len(models) > 1 else None

        # Gemini 3 models require temperature=1.0 to avoid infinite loops
        temperature = 1.0 if "gemini-3" in primary else 0.1

        config: dict = {
            "provider": "litellm",
            "config": {
                "model": primary,
                "temperature": temperature,
            },
        }

        if fallbacks:
            config["config"]["fallbacks"] = fallbacks
            config["config"]["num_retries"] = 2

        return config

    def get_embedder_config(self) -> dict:
        """Build Mem0 embedder configuration."""
        models = [m.strip() for m in self.embedder_models.split(",") if m.strip()]

        primary = models[0]

        # Parse provider/model
        if "/" in primary:
            parts = primary.split("/", 1)
            provider = parts[0]
            model = parts[1]
        else:
            provider = "openai"
            model = primary

        # Fixed 1536 dims for all models:
        # - Compatible with pgvector HNSW index (limit: 2000)
        # - Good balance between quality and storage
        # - Matryoshka models (gemini-embedding-001, text-embedding-3-*) support any dimension
        embedding_dims = 1536

        return {
            "provider": provider,
            "config": {
                "model": model,
                "embedding_dims": embedding_dims,
            },
        }

    def get_mem0_config(self) -> dict:
        """Build complete Mem0 configuration."""
        embedder_config = self.get_embedder_config()

        # Get embedding dimensions from embedder config
        embedding_dims = embedder_config.get("config", {}).get("embedding_dims", 1536)

        # Disable HNSW for dims > 2000 (pgvector HNSW limit)
        # Uses exact search instead of ANN - slower but works with any dimensions
        use_hnsw = embedding_dims <= 2000

        return {
            "vector_store": {
                "provider": "pgvector",
                "config": {
                    "collection_name": "mem0_memories",
                    "connection_string": self.database_url,
                    "embedding_model_dims": embedding_dims,
                    "hnsw": use_hnsw,
                },
            },
            "llm": self.get_llm_config(),
            "embedder": embedder_config,
        }


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
