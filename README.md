# Ansible Monorepo

Welcome to the **Ansible Monorepo**, a centralized collection of **Ansible playbooks, roles, and automation scripts** designed for streamlined infrastructure management.

## 📌 Table of Contents
1. [Overview](#-overview)
2. [Getting Started](#-getting-started)
3. [Repository Structure](#-repository-structure)
4. [Code Standards](#-code-standards)
5. [Contributing](#-contributing)
6. [Testing & CI/CD](#-testing--cicd)
7. [Versioning](#-versioning)
8. [License](#-license)

## 🌍 Overview
This repository contains **modular and reusable** Ansible configurations to automate deployment and system management. The primary goals are:
- **Idempotency**: Ensure consistent execution without unintended changes.
- **Security**: Use **1Password CLI for secrets management**.
- **Maintainability**: Follow standardized **coding and contribution** guidelines.

## 🚀 Getting Started
### Prerequisites

- **Ansible** installed:  

    ```sh
    sudo apt install ansible
    ```

- **1Password CLI** for secrets:

    ```sh 
    brew install 1password-cli  #macOS
    sudo apt install 1password-cli  #Linux
    ```

### Clone the Repo

```sh
git clone https://github.com/Masked-Kunsiquat/ansible-prime.git
cd ansible-prime
```

## 📂 Repository Structure

```sh
ansible-monorepo/
├── ansible.cfg          # Global Ansible configuration
├── inventory/           # Inventory files & groups
│   ├── hosts            # Default inventory
│   ├── group_vars/      # Group-specific variables
│   ├── host_vars/       # Host-specific variables
├── roles/               # Modular Ansible roles
├── playbooks/           # Playbooks that call roles
├── templates/           # Jinja2 templates
├── scripts/             # Supporting automation scripts
├── secrets/             # Managed via 1Password
├── CODE_STANDARDS.md    # Coding standards
├── CONTRIBUTING.md      # Contribution guidelines
├── CHANGELOG.md         # Version history
├── LICENSE              # License information
└── README.md            # This file
```


## 📝 Code Standards
All code contributions must follow the repository coding standards defined in [`CODE_STANDARDS.md`](CODE_STANDARDS.md).

## 🔧 Contributing
We welcome contributions! Please check out [`CONTRIBUTING.md`](CONTRIBUTING.md) for:

- PR & Issue Guidelines
- Branching & Commit Conventions
- CI/CD & Linting Requirements


## ✅ Testing & CI/CD
- **Pre-commit hooks** are used to enforce YAML and Ansible linting.
- GitHub Actions CI/CD automatically runs tests and linting:
    - Playbooks must pass `ansible-lint` before merging.
    - CI/CD workflows are in `.github/workflows/ci.yml`.

## 📌 Versioning
- All changes are tracked in [`CHANGELOG.md`](CHANGELOG.md).
- Releases are tagged using semantic versioning (`vX.Y.Z`).
- Run `npx semantic-release` to generate new releases.

## 📜 License
This project is licensed under the [MIT License](LICENSE).
