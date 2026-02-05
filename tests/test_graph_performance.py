import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add src to sys.path so we can import better_mem0_mcp
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from better_mem0_mcp.graph import SQLGraphStore


class TestGraphQueries(unittest.TestCase):
    def setUp(self):
        self.conn_params = {
            "dbname": "test_db",
            "user": "user",
            "password": "password",
            "host": "localhost",
        }
        self.patcher = patch("better_mem0_mcp.graph.psycopg.connect")
        self.mock_connect = self.patcher.start()

        # Mock the connection context manager
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_connect.return_value = self.mock_conn
        self.mock_conn.__enter__.return_value = self.mock_cursor

        # Mock execute return value (fetchall)
        self.mock_cursor.execute.return_value = self.mock_cursor
        # Mock some results to verify get_context processing
        self.mock_cursor.fetchall.return_value = [
            ("Label1", "Name1", "Rel1"),
            ("Label2", "Name2", "Rel2"),
        ]

    def tearDown(self):
        self.patcher.stop()

    def test_n_plus_one_query_optimized(self):
        store = SQLGraphStore(self.conn_params)

        # Query with multiple words > 3 chars
        query = "find related context for python and docker"
        # words > 3 chars: "find", "related", "context", "python", "docker" -> 5 words

        context = store.get_context(query, "user1")

        # We expect exactly 2 calls:
        # 1 call for init_tables
        # 1 call for find_related (all words in one query)
        expected_calls = 1 + 1

        print(f"Number of execute calls: {self.mock_cursor.execute.call_count}")

        self.assertEqual(self.mock_cursor.execute.call_count, expected_calls)

        # Check if the query contained ANY
        call_args = self.mock_cursor.execute.call_args_list[1]  # 0 is init, 1 is query
        sql_query = call_args[0][0]
        params = call_args[0][1]

        self.assertIn("ILIKE ANY(%s)", sql_query)
        self.assertIn("user1", params)  # user_id
        self.assertIsInstance(params[0], list)  # the patterns
        self.assertEqual(len(params[0]), 5)  # 5 patterns

        # Verify context output contains the mocked results
        self.assertIn("Name1", context)
        self.assertIn("Rel1", context)

    def test_find_related_backward_compatibility(self):
        store = SQLGraphStore(self.conn_params)
        # Reset mock calls from init
        self.mock_cursor.reset_mock()

        # Test calling with a single string
        store.find_related("single_word", "user1")

        self.assertEqual(self.mock_cursor.execute.call_count, 1)
        call_args = self.mock_cursor.execute.call_args
        sql_query = call_args[0][0]
        params = call_args[0][1]

        self.assertIn("ILIKE ANY(%s)", sql_query)
        self.assertIsInstance(params[0], list)
        self.assertEqual(len(params[0]), 1)
        self.assertEqual(params[0][0], "%single_word%")


if __name__ == "__main__":
    unittest.main()
