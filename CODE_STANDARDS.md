# Ansible Repo Coding Standards
> - Version 1.0
> - Last Updated: 2025-02-18

## Table of Contents
1. General Principles
2. Repository Structure
3. YAML & Formatting Standards
4. Variable Naming Conventions
5. Secret Management with 1Password
6. Playbook & Role Naming
7. Jinja2 Template Standards
8. Error Handling & Debugging
9. CI/CD & Linting
10. Reference in Contribution Guidelines
11. Versioning & Documentation

---

## General Principles
- **Idempotency**: Playbooks must be able to run multiple times without causing unintended changes.
- **Modularity**: Playbooks and roles should be reusable across different projects.
- **Security First**: Secrets should never be hardcoded in playbooks, templates, or inventory files.
- **Maintainability**: Keep YAML readable, formatted, and commented where necessary.

---

## Repository Structure
```
ansible-monorepo/
├── ansible.cfg         # Global Ansible configuration
├── inventory/          # Inventory files & groups
│   ├── hosts           # Default inventory
│   ├── group_vars/     # Group-specific variables
│   ├── host_vars/      # Host-specific variables
├── roles/              # Modular roles
│   ├── common/         # OS configuration role
│   │   ├── tasks/      # Role tasks
│   │   ├── handlers/   # Service handlers
│   │   ├── templates/  # Jinja2 templates
│   │   ├── defaults/   # Default variables
│   │   ├── vars/       # Role-specific variables
│   │   ├── meta/       # Role metadata
│   │   ├── files/      # Static files
├── playbooks/          # Playbooks calling roles
│   ├── main.yml        # Main entry point
├── templates/          # Jinja2 templates
│   ├── env.j2          # Environment variable template
├── scripts/            # Supporting automation scripts
├── group_vars/         # Group-wide variables
├── host_vars/          # Host-specific variables
├── secrets/            # Handled via 1Password CLI
├── README.md           # Documentation
```

---

## YAML & Formatting Standards
- **Pre-commit hooks** are enforced for:
  - YAML linting (`check-yaml`, `trailing-whitespace`, `end-of-file-fixer`).
  - Ansible linting (`ansible-lint`).
- Install pre-commit hooks locally:
  ```sh
  pip install pre-commit
  pre-commit install
  ```

---

## Variable Naming Conventions
- Use **snake_case** for variables.
- Prefix **role-specific variables** with the role name:
    ```yaml
    common_firewall_ports: [22, 80, 443]
    ```
- Use **group_vars and host_vars** instead of defining variables inline.

---

## Secret Management with 1Password
1. Setup 1Password CLI
    ```sh
    eval $(op signin my)
    ```
2. Fetch Secrets in Ansible
    ```yaml
    - name: Fetch database password from 1Password
      set_fact:
        db_password: "{{ lookup('community.general.onepassword', 'espocrm_db-pass') }}"
    ```
3. Inject Secrets into `.env` Files
    ```yaml
    - name: Create .env file
      ansible.builtin.template:
        src: env.j2
        dest: /etc/myapp/.env
        mode: '0600'
    ```

**Best Practices**:
- **Never store `.env` files in Git.** Add them to `.gitignore`.
- Use Ansible lookups for secrets instead of storing them in variables.

---

## Playbook & Role Naming
- `deploy_docker.yml` (Descriptive)
- `roles/nginx_proxy_manager/` (Self-explanatory)

---

## Jinja2 Template Standards
- Templates should be stored under `templates/` or within roles.
- Avoid hardcoding values; use variables.

Example `.env.j2` template:
```jinja2
DB_HOST={{ db_host }}
DB_USER={{ db_user }}
DB_PASSWORD={{ db_password }}
```

---

## Error Handling & Debugging
- Use `failed_when` conditions:
    ```yaml
    - name: Check service status
      ansible.builtin.command: systemctl is-active myservice
      register: service_status
      failed_when: "'active' not in service_status.stdout"
    ```
- Enable verbose mode for debugging:
    ```sh
    ansible-playbook deploy.yml -vv
    ```

---

## CI/CD & Linting
- **GitHub Actions** will automatically:
  - Run `ansible-lint` on playbooks.
  - Perform a `--check` run before merging.
- Workflow is defined in `.github/workflows/ci.yml` and must pass before merging.

### Example GitHub Actions Workflow:
```yaml
name: Ansible CI
on: [push, pull_request]

jobs:
  lint:
    name: Run Ansible Lint
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Install Ansible and Dependencies
        run: |
          sudo apt update
          sudo apt install -y ansible ansible-lint

      - name: Lint Playbooks
        run: ansible-lint playbooks/
```

---

## Reference in Contribution Guidelines
For details on how to contribute, submit PRs, and follow branch naming conventions, refer to [`CONTRIBUTING.md`](./CONTRIBUTING.md).

---

## Versioning & Documentation
- All changes are tracked in `CHANGELOG.md`.
- New releases are tagged using **semantic versioning** (`vX.Y.Z`).
- Run `npx semantic-release` to automatically generate new releases.

