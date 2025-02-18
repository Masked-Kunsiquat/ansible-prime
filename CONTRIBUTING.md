# Contributing to the Ansible Repo

Thank you for considering contributing to this project! To maintain consistency and quality across the repository, please follow the guidelines outlined below.

## Table of Contents
1. [Code Standards](#code-standards)
2. [Pull Request Guidelines](#pull-request-guidelines)
3. [Issue Reporting](#issue-reporting)
4. [Branching & Commit Conventions](#branching--commit-conventions)
5. [Testing & CI/CD](#testing--cicd)
6. [Versioning](#versioning)

## Code Standards
All code contributions must adhere to the repository's **coding standards** as defined in [`CODE_STANDARDS.md`](./CODE_STANDARDS.md). Ensure you review and follow the guidelines before submitting any changes.

## Pull Request Guidelines
- Every PR must:
  - Follow the PR template (`.github/PULL_REQUEST_TEMPLATE.md`).
  - Pass CI/CD checks before merging.
  - Be reviewed by at least one other maintainer.
- PR Naming: `feat(role_name): short description`
- Include a **clear description** of the changes and related issue references.

## Issue Reporting
- Use the provided issue template (`.github/ISSUE_TEMPLATE/bug_report.md`).
- Clearly describe the issue, including steps to reproduce and expected behavior.

## Branching & Commit Conventions
- **Branch Naming:**
  - `main` → Stable production branch.
  - `dev` → Active development.
  - `feature/<name>` → Feature-specific work.
  - `fix/<name>` → Bug fixes.
- **Commit Format:**
  ```
  <type>(<scope>): <description>
  ```
  ✅ Examples:
  - `feat(common): add firewall setup`
  - `fix(nginx): correct config path`
  - `docs(repo): update README`

## Testing & CI/CD
- Run `ansible-lint` before committing:
  ```sh
  ansible-lint playbooks/*.yml
  ```
- Pre-commit hooks must pass before code submission.
- GitHub Actions will automatically verify playbooks (`.github/workflows/ci.yml`).

## Versioning
- All changes are tracked in `CHANGELOG.md`.
- New releases are tagged using **semantic versioning** (`vX.Y.Z`).
- Run `npx semantic-release` to automatically generate new releases.

---

By following these guidelines, we ensure a clean and maintainable repository for all contributors. Happy coding! 🚀

