# [1.1.0-beta.15](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.14...v1.1.0-beta.15) (2026-01-04)


### Bug Fixes

* **ci:** verify CD workflow with beta and stable releases ([19e3150](https://github.com/n24q02m/better-mem0-mcp/commit/19e3150f903608cb57906b3f15af92df7bb29303))

# [1.1.0-beta.14](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.13...v1.1.0-beta.14) (2026-01-04)


### Bug Fixes

* add comprehensive CD workflow for semantic release, PyPI publishing, and Docker image builds, and update project version. ([1c393c6](https://github.com/n24q02m/better-mem0-mcp/commit/1c393c644756eb96e33c3e7208a6aa10054fd2f6))

# [1.1.0-beta.13](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.12...v1.1.0-beta.13) (2026-01-04)


### Bug Fixes

* **cd:** use GH_PAT to enable workflow trigger on mainUsing GITHUB_TOKEN prevents push from triggering other workflows.Using GH_PAT allows promote-to-stable to trigger CD on main branch,which then runs semantic-release to create stable releases. ([66f703d](https://github.com/n24q02m/better-mem0-mcp/commit/66f703de163934222beca65524fcb4b61e0ea2c6))

# [1.1.0-beta.12](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.11...v1.1.0-beta.12) (2026-01-04)


### Bug Fixes

* **cd:** add cd.yml to auto-resolve files list ([bd17665](https://github.com/n24q02m/better-mem0-mcp/commit/bd17665206305a4a5ac0c7641796db50cdb40776))

# [1.1.0-beta.11](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.10...v1.1.0-beta.11) (2026-01-04)


### Bug Fixes

* **setup:** don't fail when venv is locked but unusable ([ba0eae4](https://github.com/n24q02m/better-mem0-mcp/commit/ba0eae47530a26a79adb01292f2082224a89e870))

# [1.1.0-beta.10](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.9...v1.1.0-beta.10) (2026-01-04)


### Features

* **cd:** add shared scripts for promote workflow ([57a930a](https://github.com/n24q02m/better-mem0-mcp/commit/57a930a6e0021b8c7ff0c3b94a2f8d7b63cb18a0))

# [1.1.0-beta.9](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.8...v1.1.0-beta.9) (2026-01-02)


### Features

* **cd:** add Docker Hub publishing alongside GHCR ([5efb2ef](https://github.com/n24q02m/better-mem0-mcp/commit/5efb2efadbe92e651ef442f869b7d042f1fc9402))

# [1.1.0-beta.8](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.7...v1.1.0-beta.8) (2026-01-02)


### Bug Fixes

* **cd:** publish PyPI on both dev (beta) and main (stable) ([abff578](https://github.com/n24q02m/better-mem0-mcp/commit/abff5788e268f8effca5871f56ce8c1b4286cb9f))

# [1.1.0-beta.7](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.6...v1.1.0-beta.7) (2026-01-02)


### Bug Fixes

* **docker:** include README.md by not ignoring all .md files ([3bfbd29](https://github.com/n24q02m/better-mem0-mcp/commit/3bfbd29aa394f55132b178400475c0e83bcaa682))

# [1.1.0-beta.6](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.5...v1.1.0-beta.6) (2026-01-02)


### Bug Fixes

* **cd:** add debug step and explicit Dockerfile path ([8ed58c5](https://github.com/n24q02m/better-mem0-mcp/commit/8ed58c58d089fb135fe349d4ceedf1adcca469b5))

# [1.1.0-beta.5](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.4...v1.1.0-beta.5) (2026-01-02)


### Bug Fixes

* **cd:** disable Docker GHA cache to fix stale context ([5b1c7dc](https://github.com/n24q02m/better-mem0-mcp/commit/5b1c7dcff101b2fd5a052be8933db10031a615cc))

# [1.1.0-beta.4](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.3...v1.1.0-beta.4) (2026-01-02)


### Bug Fixes

* **cd:** checkout release tag for Docker build ([9f6cb29](https://github.com/n24q02m/better-mem0-mcp/commit/9f6cb29555341d6a96a538d5651a71e61d48ed45))

# [1.1.0-beta.3](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.2...v1.1.0-beta.3) (2026-01-02)


### Bug Fixes

* **docker:** include README.md in build ([537596f](https://github.com/n24q02m/better-mem0-mcp/commit/537596f4031164fb6c9267a6e87adff1f2737f36))

# [1.1.0-beta.2](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.1...v1.1.0-beta.2) (2026-01-02)


### Bug Fixes

* **cd:** capture semantic-release outputs for conditional jobs ([9d6d099](https://github.com/n24q02m/better-mem0-mcp/commit/9d6d0991143d9695dd7140e84c79b830b3ffea00))

# [1.1.0-beta.1](https://github.com/n24q02m/better-mem0-mcp/compare/v1.0.0...v1.1.0-beta.1) (2026-01-02)


### Features

* initial release with AI memory capabilities ([1dfecac](https://github.com/n24q02m/better-mem0-mcp/commit/1dfecacd84c3c0b0f25c3f2641d1d5c93f319ee6))

# 1.0.0 (2026-01-02)


### Bug Fixes

* **cd:** use built-in GITHUB_TOKEN instead of custom GH_TOKEN ([8391eb5](https://github.com/n24q02m/better-mem0-mcp/commit/8391eb5321e1a44f70c03ebaf9714d28a437b50d))
* **ci:** fix uv sync syntax and action versions ([ccc3a42](https://github.com/n24q02m/better-mem0-mcp/commit/ccc3a42200e975929085f8ca2877e37704d320da))


### Features

* implement initial better-mem0-mcp server with memory and graph stores, including project structure and CI/CD. ([12ebc03](https://github.com/n24q02m/better-mem0-mcp/commit/12ebc03ad7cb90ad9b13c4992e081278880f146b))
