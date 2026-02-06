import pytest
from unittest.mock import MagicMock, patch
import better_mem0_mcp.server as server


@pytest.mark.asyncio
async def test_memory_add_logs_masked_content():
    # Patch the global variables in the server module
    with (
        patch("better_mem0_mcp.server._settings", new_callable=MagicMock),
        patch("better_mem0_mcp.server._memory", new_callable=MagicMock) as mock_memory,
        patch("better_mem0_mcp.server._graph", new_callable=MagicMock),
        patch("better_mem0_mcp.server.logger") as mock_logger,
    ):
        mock_memory.add.return_value = "mock_result"

        content = "sensitive_password_content_that_should_not_be_logged"
        user_id = "test_user"

        # Call the memory tool directly
        result = await server.memory(action="add", content=content, user_id=user_id)

        # Verify it returns success
        assert "Saved: mock_result" in result

        # Verify sensitive content was NOT logged
        # We iterate over all calls to ensure the content is not present in any log message
        for call in mock_logger.info.call_args_list:
            args, _ = call
            log_message = args[0]
            assert content not in log_message
            assert content[:50] not in log_message

        # Verify the masked message was logged
        expected_log = (
            f"Added memory for {user_id}: [CONTENT MASKED] (length: {len(content)})"
        )
        mock_logger.info.assert_called_with(expected_log)


if __name__ == "__main__":
    import asyncio

    asyncio.run(test_memory_add_logs_masked_content())
