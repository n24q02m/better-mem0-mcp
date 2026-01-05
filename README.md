# better-mem0-mcp

**Zero-setup** MCP Server for AI memory. Works with Neon/Supabase free tier.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Quick Start

### 1. Get Prerequisites

- **Database**: [Neon](https://neon.tech) or [Supabase](https://supabase.com) (free tier)
- **API Key**: [Google AI Studio](https://aistudio.google.com/apikey) (free tier)

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
        "API_KEYS": "gemini:AIza..."
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
        "API_KEYS": "gemini:AIza..."
      }
    }
  }
}
```

### 3. Done!

Ask Claude: "Remember that I prefer dark mode and use FastAPI"

---

## Configuration

| Variable | Required | Description |
|----------|----------|-------------|
| `DATABASE_URL` | Yes | PostgreSQL connection string |
| `API_KEYS` | Yes | `provider:key,...` (multi-key per provider OK) |
| `LLM_MODELS` | No | `provider/model,...` (fallback chain) |
| `EMBEDDER_MODELS` | No | `provider/model,...` (fallback chain) |

### Examples

**Minimal (Gemini only):**
```
API_KEYS=gemini:AIza...
```

**Multi-key with fallback:**
```
API_KEYS=gemini:AIza-1,gemini:AIza-2,openai:sk-xxx
LLM_MODELS=gemini/gemini-2.5-flash,openai/gpt-4o-mini
EMBEDDER_MODELS=gemini/gemini-embedding-001,openai/text-embedding-3-small
```

### Defaults

| Setting | Default |
|---------|---------|
| `LLM_MODELS` | `gemini/gemini-2.5-flash` |
| `EMBEDDER_MODELS` | `gemini/gemini-embedding-001` |

---

## Tools

| Tool | Description |
|------|-------------|
| `memory` | `action`: add, search, list, delete |
| `help` | Detailed documentation |

### Usage

```json
{"action": "add", "content": "I prefer TypeScript over JavaScript"}
{"action": "search", "query": "preferences"}
{"action": "list"}
{"action": "delete", "memory_id": "abc123"}
```

---

## Why better-mem0-mcp?

| Feature | Official mem0-mcp | better-mem0-mcp |
|---------|-------------------|-----------------|
| Storage | Mem0 Cloud | **Self-hosted PostgreSQL** |
| Graph Memory | No | **Yes (SQL-based)** |
| LLM Provider | OpenAI only | **Any (Gemini/OpenAI/Ollama/...)** |
| Fallback | No | **Yes (multi-key + multi-model)** |
| Setup | API Key | **DATABASE_URL + API_KEYS** |

---

## License

MIT
