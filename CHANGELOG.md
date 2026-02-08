# Changelog

## [1.2.1-beta.2](https://github.com/n24q02m/better-mem0-mcp/compare/v1.2.1-beta.1...v1.2.1-beta.2) (2026-02-08)


### Documentation

* update README and project description to reflect deprecation and transition to EchoVault ([3adbfaa](https://github.com/n24q02m/better-mem0-mcp/commit/3adbfaa655a290a14605da0932fc33ef8461b553))

## [1.2.1-beta.1](https://github.com/n24q02m/better-mem0-mcp/compare/v1.2.1-beta...v1.2.1-beta.1) (2026-02-08)


### Bug Fixes

* update setup-uv action to v6 and add pytest hook to pre-commit config ([20efeeb](https://github.com/n24q02m/better-mem0-mcp/commit/20efeeb912cf751861c74f1b49f70ba57a12d93c))

## [1.2.1-beta](https://github.com/n24q02m/better-mem0-mcp/compare/v1.2.0...v1.2.1-beta) (2026-02-06)


### Bug Fixes

* add .gitattributes for consistent line endings ([0553b67](https://github.com/n24q02m/better-mem0-mcp/commit/0553b67aa2c65ae0266601b0794c5b92b2cc3fe0))
* add prerelease versioning strategy to beta config ([73e6d81](https://github.com/n24q02m/better-mem0-mcp/commit/73e6d81e243eccbcfbfb8f44a7194c3a11719874))

## [1.2.0](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0...v1.2.0) (2026-02-06)


### Features

* add development and production rulesets, update CI/CD workflows, and sync branches ([8b7724b](https://github.com/n24q02m/better-mem0-mcp/commit/8b7724b16defe27a999713adc5f9502c38231e35))
* **cd:** add Docker Hub publishing alongside GHCR ([5efb2ef](https://github.com/n24q02m/better-mem0-mcp/commit/5efb2efadbe92e651ef442f869b7d042f1fc9402))
* **cd:** add shared scripts for promote workflow ([57a930a](https://github.com/n24q02m/better-mem0-mcp/commit/57a930a6e0021b8c7ff0c3b94a2f8d7b63cb18a0))
* implement initial better-mem0-mcp server with memory and graph stores, including project structure and CI/CD. ([12ebc03](https://github.com/n24q02m/better-mem0-mcp/commit/12ebc03ad7cb90ad9b13c4992e081278880f146b))
* initial release with AI memory capabilities ([1dfecac](https://github.com/n24q02m/better-mem0-mcp/commit/1dfecacd84c3c0b0f25c3f2641d1d5c93f319ee6))


### Bug Fixes

* Add `__main__.py` entry point and update README with `better-mem0` server configuration. ([5c44f58](https://github.com/n24q02m/better-mem0-mcp/commit/5c44f58a5357c90c586009f75ddd876c45ef6f66))
* add comprehensive CD workflow for semantic release, PyPI publishing, and Docker image builds, and update project version. ([1c393c6](https://github.com/n24q02m/better-mem0-mcp/commit/1c393c644756eb96e33c3e7208a6aa10054fd2f6))
* **cd:** add cd.yml to auto-resolve files list ([bd17665](https://github.com/n24q02m/better-mem0-mcp/commit/bd17665206305a4a5ac0c7641796db50cdb40776))
* **cd:** add debug step and explicit Dockerfile path ([8ed58c5](https://github.com/n24q02m/better-mem0-mcp/commit/8ed58c58d089fb135fe349d4ceedf1adcca469b5))
* **cd:** capture semantic-release outputs for conditional jobs ([9d6d099](https://github.com/n24q02m/better-mem0-mcp/commit/9d6d0991143d9695dd7140e84c79b830b3ffea00))
* **cd:** checkout main branch for PR merge release ([77b08ad](https://github.com/n24q02m/better-mem0-mcp/commit/77b08ad425d07caf35d31730e792f54a3b961d9c))
* **cd:** checkout release tag for Docker build ([9f6cb29](https://github.com/n24q02m/better-mem0-mcp/commit/9f6cb29555341d6a96a538d5651a71e61d48ed45))
* **cd:** disable Docker GHA cache to fix stale context ([5b1c7dc](https://github.com/n24q02m/better-mem0-mcp/commit/5b1c7dcff101b2fd5a052be8933db10031a615cc))
* **cd:** publish PyPI on both dev (beta) and main (stable) ([abff578](https://github.com/n24q02m/better-mem0-mcp/commit/abff5788e268f8effca5871f56ce8c1b4286cb9f))
* **cd:** use built-in GITHUB_TOKEN instead of custom GH_TOKEN ([8391eb5](https://github.com/n24q02m/better-mem0-mcp/commit/8391eb5321e1a44f70c03ebaf9714d28a437b50d))
* **cd:** use dry-run check to prevent workflow failure when no release needed ([6cf51cd](https://github.com/n24q02m/better-mem0-mcp/commit/6cf51cd7cfb8475a834f3547625d1ca328997d44))
* **cd:** use GH_PAT to enable workflow trigger on mainUsing GITHUB_TOKEN prevents push from triggering other workflows.Using GH_PAT allows promote-to-stable to trigger CD on main branch,which then runs semantic-release to create stable releases. ([66f703d](https://github.com/n24q02m/better-mem0-mcp/commit/66f703de163934222beca65524fcb4b61e0ea2c6))
* **ci:** fix uv sync syntax and action versions ([ccc3a42](https://github.com/n24q02m/better-mem0-mcp/commit/ccc3a42200e975929085f8ca2877e37704d320da))
* **ci:** verify CD workflow with beta and stable releases ([19e3150](https://github.com/n24q02m/better-mem0-mcp/commit/19e3150f903608cb57906b3f15af92df7bb29303))
* correct Mem0 API response parsing for search and get_all ([8a612b1](https://github.com/n24q02m/better-mem0-mcp/commit/8a612b1443c59c229e7583ffedced6d38f1b13d1))
* correct search response parsing and improve documentation ([d4d4753](https://github.com/n24q02m/better-mem0-mcp/commit/d4d4753a7d0d3c8eb23ef15c051a7bcb1b000310))
* correct semantic-release outputs detection ([eecfeea](https://github.com/n24q02m/better-mem0-mcp/commit/eecfeea50c9d4a758f6810d5989ae4c1eaf1398a))
* **docker:** include README.md by not ignoring all .md files ([3bfbd29](https://github.com/n24q02m/better-mem0-mcp/commit/3bfbd29aa394f55132b178400475c0e83bcaa682))
* **docker:** include README.md in build ([537596f](https://github.com/n24q02m/better-mem0-mcp/commit/537596f4031164fb6c9267a6e87adff1f2737f36))
* Pin Python version to 3.13 and remove Python 3.14 compatibility from the dependency lock file. ([ec134ef](https://github.com/n24q02m/better-mem0-mcp/commit/ec134ef10ab6de3eaf800d51a441fe2b44f2d4dc))
* **setup:** don't fail when venv is locked but unusable ([ba0eae4](https://github.com/n24q02m/better-mem0-mcp/commit/ba0eae47530a26a79adb01292f2082224a89e870))
* update Node.js version to 24 in CI/CD configuration and Mise setup ([92ab0a9](https://github.com/n24q02m/better-mem0-mcp/commit/92ab0a96cd30643b9ecf927c68b46cde6472d732))
* Use GITHUB_TOKEN instead of GH_PAT for GitHub Container Registry authentication and CI/CD status checks. ([2287b07](https://github.com/n24q02m/better-mem0-mcp/commit/2287b072b1ea9f96fb466abb6497d45363b5052d))
* verify ci/cd workflow changes ([dfb6480](https://github.com/n24q02m/better-mem0-mcp/commit/dfb6480f13721a04606a3246947af5fd0764cc6a))


### Documentation

* Add Code of Conduct and enhance project documentation with detailed features, setup, and security reporting guidelines. ([ee8e33e](https://github.com/n24q02m/better-mem0-mcp/commit/ee8e33e414864a933e6207b9226d5eaec1068acb))

## [1.1.0-beta.25](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.24...v1.1.0-beta.25) (2026-02-05)


### Bug Fixes

* **cd:** use dry-run check to prevent workflow failure when no release needed ([6cf51cd](https://github.com/n24q02m/better-mem0-mcp/commit/6cf51cd7cfb8475a834f3547625d1ca328997d44))

## [1.1.0-beta.24](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.23...v1.1.0-beta.24) (2026-02-05)


### Bug Fixes

* **cd:** checkout main branch for PR merge release ([77b08ad](https://github.com/n24q02m/better-mem0-mcp/commit/77b08ad425d07caf35d31730e792f54a3b961d9c))

## [1.1.0-beta.23](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.22...v1.1.0-beta.23) (2026-02-05)


### Bug Fixes

* Use GITHUB_TOKEN instead of GH_PAT for GitHub Container Registry authentication and CI/CD status checks. ([2287b07](https://github.com/n24q02m/better-mem0-mcp/commit/2287b072b1ea9f96fb466abb6497d45363b5052d))

## [1.1.0-beta.22](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.21...v1.1.0-beta.22) (2026-02-05)


### Bug Fixes

* Pin Python version to 3.13 and remove Python 3.14 compatibility from the dependency lock file. ([ec134ef](https://github.com/n24q02m/better-mem0-mcp/commit/ec134ef10ab6de3eaf800d51a441fe2b44f2d4dc))

## [1.1.0-beta.21](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.20...v1.1.0-beta.21) (2026-01-12)


### Bug Fixes

* update Node.js version to 24 in CI/CD configuration and Mise setup ([92ab0a9](https://github.com/n24q02m/better-mem0-mcp/commit/92ab0a96cd30643b9ecf927c68b46cde6472d732))

## [1.1.0-beta.20](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.19...v1.1.0-beta.20) (2026-01-05)


### Bug Fixes

* correct search response parsing and improve documentation ([d4d4753](https://github.com/n24q02m/better-mem0-mcp/commit/d4d4753a7d0d3c8eb23ef15c051a7bcb1b000310))

## [1.1.0-beta.19](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.18...v1.1.0-beta.19) (2026-01-05)


### Bug Fixes

* correct Mem0 API response parsing for search and get_all ([8a612b1](https://github.com/n24q02m/better-mem0-mcp/commit/8a612b1443c59c229e7583ffedced6d38f1b13d1))

## [1.1.0-beta.18](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.17...v1.1.0-beta.18) (2026-01-05)


### Bug Fixes

* Add `__main__.py` entry point and update README with `better-mem0` server configuration. ([5c44f58](https://github.com/n24q02m/better-mem0-mcp/commit/5c44f58a5357c90c586009f75ddd876c45ef6f66))

## [1.1.0-beta.17](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.16...v1.1.0-beta.17) (2026-01-05)


### Bug Fixes

* correct semantic-release outputs detection ([eecfeea](https://github.com/n24q02m/better-mem0-mcp/commit/eecfeea50c9d4a758f6810d5989ae4c1eaf1398a))

## [1.1.0-beta.16](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.15...v1.1.0-beta.16) (2026-01-05)


### Bug Fixes

* verify ci/cd workflow changes ([dfb6480](https://github.com/n24q02m/better-mem0-mcp/commit/dfb6480f13721a04606a3246947af5fd0764cc6a))

## [1.1.0-beta.15](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.14...v1.1.0-beta.15) (2026-01-04)


### Bug Fixes

* **ci:** verify CD workflow with beta and stable releases ([19e3150](https://github.com/n24q02m/better-mem0-mcp/commit/19e3150f903608cb57906b3f15af92df7bb29303))

## [1.1.0-beta.14](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.13...v1.1.0-beta.14) (2026-01-04)


### Bug Fixes

* add comprehensive CD workflow for semantic release, PyPI publishing, and Docker image builds, and update project version. ([1c393c6](https://github.com/n24q02m/better-mem0-mcp/commit/1c393c644756eb96e33c3e7208a6aa10054fd2f6))

## [1.1.0-beta.13](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.12...v1.1.0-beta.13) (2026-01-04)


### Bug Fixes

* **cd:** use GH_PAT to enable workflow trigger on mainUsing GITHUB_TOKEN prevents push from triggering other workflows.Using GH_PAT allows promote-to-stable to trigger CD on main branch,which then runs semantic-release to create stable releases. ([66f703d](https://github.com/n24q02m/better-mem0-mcp/commit/66f703de163934222beca65524fcb4b61e0ea2c6))

## [1.1.0-beta.12](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.11...v1.1.0-beta.12) (2026-01-04)


### Bug Fixes

* **cd:** add cd.yml to auto-resolve files list ([bd17665](https://github.com/n24q02m/better-mem0-mcp/commit/bd17665206305a4a5ac0c7641796db50cdb40776))

## [1.1.0-beta.11](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.10...v1.1.0-beta.11) (2026-01-04)


### Bug Fixes

* **setup:** don't fail when venv is locked but unusable ([ba0eae4](https://github.com/n24q02m/better-mem0-mcp/commit/ba0eae47530a26a79adb01292f2082224a89e870))

## [1.1.0-beta.10](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.9...v1.1.0-beta.10) (2026-01-04)


### Features

* **cd:** add shared scripts for promote workflow ([57a930a](https://github.com/n24q02m/better-mem0-mcp/commit/57a930a6e0021b8c7ff0c3b94a2f8d7b63cb18a0))

## [1.1.0-beta.9](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.8...v1.1.0-beta.9) (2026-01-02)


### Features

* **cd:** add Docker Hub publishing alongside GHCR ([5efb2ef](https://github.com/n24q02m/better-mem0-mcp/commit/5efb2efadbe92e651ef442f869b7d042f1fc9402))

## [1.1.0-beta.8](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.7...v1.1.0-beta.8) (2026-01-02)


### Bug Fixes

* **cd:** publish PyPI on both dev (beta) and main (stable) ([abff578](https://github.com/n24q02m/better-mem0-mcp/commit/abff5788e268f8effca5871f56ce8c1b4286cb9f))

## [1.1.0-beta.7](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.6...v1.1.0-beta.7) (2026-01-02)


### Bug Fixes

* **docker:** include README.md by not ignoring all .md files ([3bfbd29](https://github.com/n24q02m/better-mem0-mcp/commit/3bfbd29aa394f55132b178400475c0e83bcaa682))

## [1.1.0-beta.6](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.5...v1.1.0-beta.6) (2026-01-02)


### Bug Fixes

* **cd:** add debug step and explicit Dockerfile path ([8ed58c5](https://github.com/n24q02m/better-mem0-mcp/commit/8ed58c58d089fb135fe349d4ceedf1adcca469b5))

## [1.1.0-beta.5](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.4...v1.1.0-beta.5) (2026-01-02)


### Bug Fixes

* **cd:** disable Docker GHA cache to fix stale context ([5b1c7dc](https://github.com/n24q02m/better-mem0-mcp/commit/5b1c7dcff101b2fd5a052be8933db10031a615cc))

## [1.1.0-beta.4](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.3...v1.1.0-beta.4) (2026-01-02)


### Bug Fixes

* **cd:** checkout release tag for Docker build ([9f6cb29](https://github.com/n24q02m/better-mem0-mcp/commit/9f6cb29555341d6a96a538d5651a71e61d48ed45))

## [1.1.0-beta.3](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.2...v1.1.0-beta.3) (2026-01-02)


### Bug Fixes

* **docker:** include README.md in build ([537596f](https://github.com/n24q02m/better-mem0-mcp/commit/537596f4031164fb6c9267a6e87adff1f2737f36))

## [1.1.0-beta.2](https://github.com/n24q02m/better-mem0-mcp/compare/v1.1.0-beta.1...v1.1.0-beta.2) (2026-01-02)


### Bug Fixes

* **cd:** capture semantic-release outputs for conditional jobs ([9d6d099](https://github.com/n24q02m/better-mem0-mcp/commit/9d6d0991143d9695dd7140e84c79b830b3ffea00))

## [1.1.0-beta.1](https://github.com/n24q02m/better-mem0-mcp/compare/v1.0.0...v1.1.0-beta.1) (2026-01-02)


### Features

* initial release with AI memory capabilities ([1dfecac](https://github.com/n24q02m/better-mem0-mcp/commit/1dfecacd84c3c0b0f25c3f2641d1d5c93f319ee6))

## 1.0.0 (2026-01-02)


### Bug Fixes

* **cd:** use built-in GITHUB_TOKEN instead of custom GH_TOKEN ([8391eb5](https://github.com/n24q02m/better-mem0-mcp/commit/8391eb5321e1a44f70c03ebaf9714d28a437b50d))
* **ci:** fix uv sync syntax and action versions ([ccc3a42](https://github.com/n24q02m/better-mem0-mcp/commit/ccc3a42200e975929085f8ca2877e37704d320da))


### Features

* implement initial better-mem0-mcp server with memory and graph stores, including project structure and CI/CD. ([12ebc03](https://github.com/n24q02m/better-mem0-mcp/commit/12ebc03ad7cb90ad9b13c4992e081278880f146b))
