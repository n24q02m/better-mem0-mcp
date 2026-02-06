"""
better-mem0-mcp MCP Server.

Tiered Description Pattern:
- Tier 1: Compressed descriptions in tool definitions (~150 tokens)
- Tier 2: Full docs via `help` tool (on-demand, ~500 tokens)
- Tier 3: MCP Resources for supported clients
"""

from functools import lru_cache
from pathlib import Path

from loguru import logger
from mcp.server.fastmcp import FastMCP

from .config import get_settings

# Initialize MCP Server
mcp = FastMCP("better-mem0-mcp")

# Lazy-initialized globals
_memory = None
_graph = None
_settings = None

DEFAULT_USER = "default"


def _init():
    """Lazy initialization of memory and graph stores."""
    global _memory, _graph, _settings

    if _settings is not None:
        return

    _settings = get_settings()

    # Validate required settings
    if not _settings.database_url:
        raise ValueError("DATABASE_URL is required")
    if not _settings.api_keys:
        raise ValueError("API_KEYS is required")

    # Setup API keys (sets env vars for LiteLLM)
    keys_by_provider = _settings.setup_api_keys()
    logger.info(f"API keys configured for: {list(keys_by_provider.keys())}")

    # Initialize Mem0 Memory (Vector Store)
    from mem0 import Memory

    mem0_config = _settings.get_mem0_config()
    _memory = Memory.from_config(mem0_config)
    logger.info(f"Vector Memory initialized: {_settings.llm_models.split(',')[0]}")

    # Initialize Graph Store (SQL-based)
    try:
        from .graph import SQLGraphStore

        _graph = SQLGraphStore(_settings.parse_database_url())
        logger.info("Graph Memory initialized (SQL)")
    except Exception as e:
        logger.warning(f"Graph Memory disabled: {e}")


@lru_cache
def _load_doc(name: str) -> str:
    """Load documentation file from docs/ directory."""
    docs_dir = Path(__file__).parent / "docs"
    doc_file = docs_dir / f"{name}.md"
    if doc_file.exists():
        return doc_file.read_text()
    return f"Documentation not found: {name}"


# =============================================================================
# Tool: memory
# Tier 1: Compressed description
# =============================================================================
@mcp.tool()
async def memory(
    action: str,
    content: str | None = None,
    query: str | None = None,
    memory_id: str | None = None,
    user_id: str | None = None,
    limit: int = 5,
) -> str:
    """
    Memory operations: add, search, list, delete.
    - add: Save information (requires content)
    - search: Find memories (requires query)
    - list: Get all memories
    - delete: Remove by ID (requires memory_id)
    Use `help` tool for full documentation.
    """
    _init()

    user_id = user_id or DEFAULT_USER

    try:
        if action == "add":
            if not content:
                return "Error: 'content' required for add action"

            result = _memory.add(content, user_id=user_id)
            logger.info(f"Added memory for {user_id}: {content[:50]}...")
            return f"Saved: {result}"

        elif action == "search":
            if not query:
                return "Error: 'query' required for search action"

            # Vector search - returns {"results": [...]} (same as get_all)
            response = _memory.search(query, user_id=user_id, limit=limit)
            memories = (
                response.get("results", []) if isinstance(response, dict) else response
            )

            # Add graph context
            graph_context = ""
            if _graph:
                graph_context = _graph.get_context(query, user_id)

            if not memories and not graph_context:
                return "No memories found."

            output = ""
            if memories:
                output = "Memories:\n" + "\n".join(
                    [f"- {m.get('memory', str(m))}" for m in memories]
                )
            if graph_context:
                output += f"\n\n{graph_context}"

            return output

        elif action == "list":
            # get_all returns {"results": [...]} or list directly
            response = _memory.get_all(user_id=user_id)
            memories = (
                response.get("results", []) if isinstance(response, dict) else response
            )

            if not memories:
                return "No memories stored."

            lines = [f"- [{m['id'][:8]}] {m['memory']}" for m in memories]
            return f"Memories ({len(memories)}):\n" + "\n".join(lines)

        elif action == "delete":
            if not memory_id:
                return "Error: 'memory_id' required for delete action"

            _memory.delete(memory_id)
            logger.info(f"Deleted memory: {memory_id}")
            return f"Deleted: {memory_id}"

        else:
            return f"Unknown action: {action}. Use: add, search, list, delete"

    except Exception as e:
        logger.error(f"Memory operation failed: {e}")
        return f"Error: {e}"


# =============================================================================
# Tool: help
# Tier 2: Full documentation on-demand
# =============================================================================
@mcp.tool()
async def help(tool_name: str = "memory") -> str:
    """
    Get full documentation for a tool.
    Use when compressed descriptions are insufficient.
    """
    return _load_doc(tool_name)


def main():
    """Entry point for MCP server."""
    logger.info("Starting better-mem0-mcp server (stdio)")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
