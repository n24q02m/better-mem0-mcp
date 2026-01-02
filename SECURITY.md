# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.x.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it by:

1. **Do NOT** create a public GitHub issue
2. Email the maintainer directly or use GitHub's private vulnerability reporting
3. Include detailed steps to reproduce the issue
4. Allow reasonable time for a fix before public disclosure

We take security seriously and will respond promptly to valid reports.

## Security Best Practices

When using better-mem0-mcp:

- **Never commit API keys** to version control
- Use environment variables or secure secret management
- Keep dependencies updated
- Use `sslmode=require` for production database connections
