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

### search
Semantic search across stored memories. Combines vector search with graph context.

```json
{"action": "search", "query": "coding preferences", "limit": 5}
```

### list
Get all stored memories for a user.

```json
{"action": "list"}
```

### delete
Remove a memory by ID.

```json
{"action": "delete", "memory_id": "abc12345-..."}
```

## Parameters
- `action` - Required: add, search, list, delete
- `content` - Required for add: information to remember
- `query` - Required for search: what to search for
- `memory_id` - Required for delete: ID of memory to remove
- `limit` - Optional for search: max results (default: 5)
- `user_id` - Optional: scope memories to a specific user
