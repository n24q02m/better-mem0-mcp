
## 2025-05-26 - [Path Traversal in Documentation Loader]
**Vulnerability:** The `_load_doc` function allowed directory traversal via `../` sequences in the `name` parameter, potentially exposing sensitive files on the server.
**Learning:** `pathlib.Path` concatenation (`/`) does not automatically prevent traversal. A path like `base / "../target"` is valid and can point outside `base`.
**Prevention:** Always use `.resolve()` on both the base directory and the target path, then verify the target path is within the base directory using `.is_relative_to()`. Input validation (e.g., alphanumeric only) adds defense-in-depth.
