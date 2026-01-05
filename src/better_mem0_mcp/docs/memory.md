# memory - Full Documentation

## Overview
Memory operations for AI agents: add, search, list, delete.

Uses Mem0 for vector memory (pgvector) and SQL-based graph storage.

## Actions

### add
Save information to long-term memory. Mem0 automatically:
- Extracts key facts
- Creates embeddings for semantic search
- Deduplicates similar memories

```json
{"action": "add", "content": "User prefers dark mode and uses FastAPI"}
```

**Response:** `Saved: {results: [{id, memory, event}]}`

### search
Semantic search across stored memories. Combines vector search with graph context.

```json
{"action": "search", "query": "coding preferences", "limit": 5}
```

**Response:** Formatted list of matching memories with optional graph context.

### list
Get all stored memories for a user.

```json
{"action": "list"}
```

**Response:** `Memories (N): - [id] memory text`

### delete
Remove a memory by ID.

```json
{"action": "delete", "memory_id": "abc12345-..."}
```

**Response:** `Deleted: {memory_id}`

## Parameters
- `action` - Required: add, search, list, delete
- `content` - Required for add: information to remember
- `query` - Required for search: what to search for
- `memory_id` - Required for delete: ID of memory to remove
- `limit` - Optional for search: max results (default: 5)
- `user_id` - Optional: scope memories to a specific user (default: "default")

## Technical Notes
- Mem0 API returns `{"results": [...]}` for both `search()` and `get_all()`
- Graph context is automatically included in search results when available
- Embeddings use 1536 dimensions for pgvector HNSW compatibility
