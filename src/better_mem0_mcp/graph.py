"""SQL-based Graph Storage - works with any PostgreSQL, no extensions needed."""

from typing import Any

import psycopg
from loguru import logger


class SQLGraphStore:
    """Graph storage using plain SQL tables (nodes + edges)."""

    INIT_SQL = """
    CREATE TABLE IF NOT EXISTS graph_nodes (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        label VARCHAR(50) NOT NULL,
        name VARCHAR(255),
        properties JSONB DEFAULT '{}',
        user_id VARCHAR(100) NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW()
    );

    CREATE TABLE IF NOT EXISTS graph_edges (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        from_node_id UUID REFERENCES graph_nodes(id) ON DELETE CASCADE,
        to_node_id UUID REFERENCES graph_nodes(id) ON DELETE CASCADE,
        relationship VARCHAR(100) NOT NULL,
        properties JSONB DEFAULT '{}',
        created_at TIMESTAMPTZ DEFAULT NOW()
    );

    CREATE INDEX IF NOT EXISTS idx_graph_nodes_user ON graph_nodes(user_id);
    CREATE INDEX IF NOT EXISTS idx_graph_nodes_name ON graph_nodes(name);
    CREATE INDEX IF NOT EXISTS idx_graph_nodes_label ON graph_nodes(label);
    CREATE INDEX IF NOT EXISTS idx_graph_edges_from ON graph_edges(from_node_id);
    CREATE INDEX IF NOT EXISTS idx_graph_edges_to ON graph_edges(to_node_id);
    CREATE INDEX IF NOT EXISTS idx_graph_edges_rel ON graph_edges(relationship);
    """

    def __init__(self, conn_params: dict[str, Any]):
        """Initialize graph store with database connection parameters."""
        self.conn_params = {
            k: v
            for k, v in conn_params.items()
            if k in ("host", "port", "dbname", "user", "password")
        }
        # Add sslmode if present
        if "sslmode" in conn_params:
            self.conn_params["sslmode"] = conn_params["sslmode"]
        self._init_tables()

    def _get_connection(self):
        """Get a new database connection."""
        return psycopg.connect(**self.conn_params)

    def _init_tables(self):
        """Initialize graph tables if not exist."""
        try:
            with self._get_connection() as conn:
                conn.execute(self.INIT_SQL)
                conn.commit()
            logger.info("Graph tables initialized")
        except Exception as e:
            logger.warning(f"Graph init failed (may already exist): {e}")

    def add_node(
        self,
        label: str,
        name: str,
        user_id: str,
        properties: dict | None = None,
    ) -> str | None:
        """Add or get existing node. Returns node ID."""
        try:
            with self._get_connection() as conn:
                # Check if exists
                result = conn.execute(
                    "SELECT id FROM graph_nodes WHERE label = %s AND name = %s AND user_id = %s",
                    (label, name, user_id),
                ).fetchone()

                if result:
                    return str(result[0])

                # Create new
                from psycopg.types.json import Json

                result = conn.execute(
                    """INSERT INTO graph_nodes (label, name, properties, user_id)
                       VALUES (%s, %s, %s, %s) RETURNING id""",
                    (label, name, Json(properties or {}), user_id),
                ).fetchone()
                conn.commit()
                return str(result[0]) if result else None
        except Exception as e:
            logger.error(f"Failed to add node: {e}")
            return None

    def add_edge(
        self,
        from_id: str,
        to_id: str,
        relationship: str,
        properties: dict | None = None,
    ) -> bool:
        """Add edge between nodes."""
        try:
            with self._get_connection() as conn:
                from psycopg.types.json import Json

                conn.execute(
                    """INSERT INTO graph_edges (from_node_id, to_node_id, relationship, properties)
                       VALUES (%s, %s, %s, %s)
                       ON CONFLICT DO NOTHING""",
                    (from_id, to_id, relationship, Json(properties or {})),
                )
                conn.commit()
                return True
        except Exception as e:
            logger.error(f"Failed to add edge: {e}")
            return False

    def find_related(self, name: str, user_id: str, limit: int = 10) -> list[dict]:
        """Find nodes related to a name."""
        try:
            with self._get_connection() as conn:
                results = conn.execute(
                    """
                    SELECT DISTINCT n2.label, n2.name, e.relationship
                    FROM graph_nodes n1
                    JOIN graph_edges e ON n1.id = e.from_node_id OR n1.id = e.to_node_id
                    JOIN graph_nodes n2 ON (e.to_node_id = n2.id OR e.from_node_id = n2.id)
                        AND n2.id != n1.id
                    WHERE n1.name ILIKE %s AND n1.user_id = %s
                    LIMIT %s
                    """,
                    (f"%{name}%", user_id, limit),
                ).fetchall()

                return [
                    {"label": r[0], "name": r[1], "relationship": r[2]} for r in results
                ]
        except Exception as e:
            logger.error(f"Failed to find related: {e}")
            return []

    def get_context(self, query: str, user_id: str) -> str:
        """Get graph context for a query (find related entities)."""
        words = [w for w in query.split() if len(w) > 3]
        related: list[dict] = []

        for word in words[:5]:  # Limit to first 5 significant words
            related.extend(self.find_related(word, user_id, limit=3))

        if not related:
            return ""

        # Deduplicate
        seen = set()
        unique = []
        for r in related:
            key = (r["name"], r["relationship"])
            if key not in seen:
                seen.add(key)
                unique.append(r)

        if not unique:
            return ""

        lines = [
            f"- {r['name']} ({r['label']}) - {r['relationship']}" for r in unique[:5]
        ]
        return "Related context:\n" + "\n".join(lines)
