# Contributing to better-mem0-mcp

Thank you for your interest in contributing to better-mem0-mcp! This guide will help you get started.

## Getting Started

### Prerequisites

- **mise** (recommended) or **Python 3.13+** and **uv**
- Git
- A GitHub account

**Recommended:** Use [mise](https://mise.jdx.dev/) to automatically manage Python and uv versions from `.mise.toml`.

### Setup Development Environment

1. **Fork the repository** and clone your fork

```bash
git clone https://github.com/YOUR_USERNAME/better-mem0-mcp
cd better-mem0-mcp
```

2. **Install tools and dependencies**

If using **mise** (recommended):

```bash
mise run setup
```

Without mise, ensure you have Python 3.13+ and uv installed:

```bash
uv sync --dev
uv run pre-commit install
```

3. **Run checks**

```bash
uv run ruff check .
uv run ruff format --check .
```

## Development Workflow

### Running Locally

```bash
# Set your environment variables
export DATABASE_URL="postgresql://..."
export API_KEYS="gemini:AIza..."

# Run the server
uv run better-mem0-mcp
```

### Making Changes

1. Create a new branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Run checks: `uv run ruff check . && uv run ruff format .`
4. Run tests: `uv run pytest`
5. Commit your changes (see [Commit Convention](#commit-convention))
6. Push to your fork: `git push origin feature/your-feature-name`
7. Open a Pull Request

## Commit Convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

```text
<type>[optional scope]: <description>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```text
feat: add support for Anthropic API
fix: handle database connection timeout
docs: update configuration examples
```

## Code Style

This project uses **Ruff** for formatting and linting.

```bash
uv run ruff check .       # Check for issues
uv run ruff check --fix . # Auto-fix issues
uv run ruff format .      # Format code
```

## Testing

```bash
uv run pytest              # Run all tests
uv run pytest -v           # Verbose output
uv run pytest --tb=short   # Short tracebacks
```

## Project Structure

```text
better-mem0-mcp/
├── src/
│   └── better_mem0_mcp/
│       ├── __init__.py
│       ├── config.py      # Configuration
│       ├── graph.py       # SQL graph store
│       └── server.py      # MCP server
├── tests/
├── pyproject.toml
└── README.md
```

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing! 🎉**
