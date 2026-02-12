# better-mem0-mcp

> [!CAUTION]
> **PROJECT DISCONTINUED** — The replacement solution is being developed at [mnemo-mcp](https://github.com/n24q02m/mnemo-mcp).

**Self-hosted MCP Server for AI memory with PostgreSQL (pgvector).**

[![PyPI](https://img.shields.io/pypi/v/better-mem0-mcp)](https://pypi.org/project/better-mem0-mcp/)
[![Docker](https://img.shields.io/docker/v/n24q02m/better-mem0-mcp?label=docker)](https://hub.docker.com/r/n24q02m/better-mem0-mcp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Discontinuation Notice

The `better-mem0-mcp` project has been **discontinued** as of February 2026.

The replacement solution is being developed at **[mnemo-mcp](https://github.com/n24q02m/mnemo-mcp)** — a lightweight, self-hosted MCP server for persistent AI memory.

---

## Legacy Documentation

> [!NOTE]
> The content below is kept for reference. The final version on PyPI/Docker still works but will **not receive any new updates**.

## Features

- **Self-hosted PostgreSQL** - Your data stays with you (Neon/Supabase free tier supported)
- **Graph Memory** - SQL-based relationship tracking alongside vector memory
- **Multi-provider LLM** - Gemini, OpenAI, Anthropic, Groq, DeepSeek, Mistral
- **Fallback chains** - Multi-key per provider + multi-model fallback
- **Zero manual setup** - Just `DATABASE_URL` + `API_KEYS`

---

<details>
<summary><strong>Quick Start (Legacy)</strong></summary>

### 1. Get Prerequisites

- **Database**: [Neon](https://neon.tech) or [Supabase](https://supabase.com) (free tier works)
- **API Key**: Any supported provider ([Google AI Studio](https://aistudio.google.com/apikey) is free)

### 2. Add to mcp.json

#### uvx (Recommended)

```json
{
  "mcpServers": {
    "better-mem0": {
      "command": "uvx",
      "args": ["better-mem0-mcp@latest"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@xxx.neon.tech/neondb?sslmode=require",
        "API_KEYS": "GOOGLE_API_KEY:AIza..."
      }
    }
  }
}
```

#### Docker

```json
{
  "mcpServers": {
    "better-mem0": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "DATABASE_URL", "-e", "API_KEYS", "n24q02m/better-mem0-mcp:latest"],
      "env": {
        "DATABASE_URL": "postgresql://...",
        "API_KEYS": "GOOGLE_API_KEY:AIza..."
      }
    }
  }
}
```

### 3. Done!

Ask your AI: "Remember that I prefer dark mode and use FastAPI"

</details>

<details>
<summary><strong>Configuration (Legacy)</strong></summary>

| Variable | Required | Description |
|----------|----------|-------------|
| `DATABASE_URL` | Yes | PostgreSQL with pgvector extension |
| `API_KEYS` | Yes | `ENV_VAR:key` pairs, comma-separated |
| `LLM_MODELS` | No | Model fallback chain |
| `EMBEDDER_MODELS` | No | Embedding model chain |

### Supported LiteLLM Providers

Use environment variable names from [LiteLLM docs](https://docs.litellm.ai/):
`GOOGLE_API_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GROQ_API_KEY`, etc.

**Single provider:**
```bash
API_KEYS=GOOGLE_API_KEY:AIza...
```

**Multi-key with fallback:**
```bash
API_KEYS=GOOGLE_API_KEY:AIza-1,GOOGLE_API_KEY:AIza-2,OPENAI_API_KEY:sk-xxx
LLM_MODELS=gemini/gemini-3-flash-preview,openai/gpt-4o-mini
EMBEDDER_MODELS=gemini/gemini-embedding-001,openai/text-embedding-3-small
```

### Defaults

| Setting | Default |
|---------|---------|
| `LLM_MODELS` | `gemini/gemini-3-flash-preview` |
| `EMBEDDER_MODELS` | `gemini/gemini-embedding-001` |

</details>

<details>
<summary><strong>Tools (Legacy)</strong></summary>

| Tool | Description |
|------|-------------|
| `memory` | Memory operations: `add`, `search`, `list`, `delete` |
| `help` | Get full documentation for tools |

### Usage Examples

```json
{"action": "add", "content": "I prefer TypeScript over JavaScript"}
{"action": "search", "query": "programming preferences"}
{"action": "list"}
{"action": "delete", "memory_id": "abc123"}
```

</details>

<details>
<summary><strong>Build from Source (Legacy)</strong></summary>

```bash
git clone https://github.com/n24q02m/better-mem0-mcp
cd better-mem0-mcp

# Setup (requires mise: https://mise.jdx.dev/)
mise run setup

# Run
uv run better-mem0-mcp
```

**Requirements:** Python 3.13+

</details>

---

## License

MIT - See [LICENSE](LICENSE)
