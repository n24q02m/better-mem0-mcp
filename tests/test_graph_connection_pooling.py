import sys
import unittest
from unittest.mock import MagicMock, patch

# Add src to path
sys.path.append("src")

from better_mem0_mcp.graph import SQLGraphStore

class TestSQLGraphStoreOptimization(unittest.TestCase):
    @patch('better_mem0_mcp.graph.ConnectionPool')
    def test_connection_pooling(self, MockPool):
        # Setup mock pool
        mock_pool_instance = MagicMock()
        MockPool.return_value = mock_pool_instance

        # Setup mock connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()

        # When pool.connection() is called, it returns a context manager that yields mock_conn
        mock_connection_ctx = MagicMock()
        mock_connection_ctx.__enter__.return_value = mock_conn
        mock_pool_instance.connection.return_value = mock_connection_ctx

        mock_conn.execute.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None

        # Initialize store
        store = SQLGraphStore({"dbname": "test"})

        # Verify pool was initialized
        MockPool.assert_called_once()

        # Simulate adding multiple nodes
        for i in range(5):
            store.add_node("test_label", f"node_{i}", "user_1")

        # Check that pool.connection() was called
        # 1 call from _init_tables (inside __init__)
        # 5 calls from add_node
        # Total 6 calls to pool.connection()

        self.assertEqual(mock_pool_instance.connection.call_count, 6)
        print(f"ConnectionPool.connection() called {mock_pool_instance.connection.call_count} times")

if __name__ == '__main__':
    unittest.main()
