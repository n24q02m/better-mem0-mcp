import pytest
from pathlib import Path
from better_mem0_mcp.server import _load_doc

def test_load_doc_valid():
    """Test loading a valid document."""
    # Ensure memory.md exists for this test to pass
    docs_dir = Path("src/better_mem0_mcp/docs")
    if not (docs_dir / "memory.md").exists():
        pytest.skip("memory.md not found, skipping valid doc test")

    content = _load_doc("memory")
    # Content should contain something from the doc
    assert content
    assert "Documentation not found" not in content
    assert "Access denied" not in content

def test_load_doc_not_found():
    """Test loading a non-existent document."""
    content = _load_doc("nonexistent_doc")
    assert "Documentation not found" in content

def test_load_doc_path_traversal():
    """Test path traversal attempt."""
    content = _load_doc("../../../README")
    assert "Access denied" in content

    content = _load_doc("../something")
    assert "Access denied" in content
