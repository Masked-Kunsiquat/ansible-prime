# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Ansible monorepo designed for **homelab disaster recovery**. The primary goal is to quickly spin up a complete homelab environment from scratch, focusing on Proxmox LXC provisioning and media server stack deployment. The repository emphasizes simplicity, idempotency, and 1Password CLI integration for secrets.

## Development Commands

### Linting and Testing
```bash
# Install pre-commit hooks (required for development)
pip install pre-commit
pre-commit install

# Lint Ansible playbooks
ansible-lint playbooks/*.yml

# Run Ansible playbook in check mode (dry run)
ansible-playbook playbooks/main.yml --check

# Run with verbose output for debugging
ansible-playbook playbooks/main.yml -vv
```

### Release Management
```bash
# Generate new semantic release
npx semantic-release
```

## Repository Structure

The repository follows a standard Ansible monorepo structure:

- `inventory/` - Inventory files with `hosts`, `group_vars/`, and `host_vars/`
- `roles/` - Modular Ansible roles (each role should have standard subdirectories: `tasks/`, `handlers/`, `templates/`, `defaults/`, `vars/`, `meta/`, `files/`)
- `playbooks/` - Playbooks that orchestrate roles, with `main.yml` as the primary entry point
- `templates/` - Global Jinja2 templates
- `scripts/` - Supporting automation scripts
- `secrets/` - Managed via 1Password CLI (never commit actual secrets)

## Homelab Environment

**Current Infrastructure:**
- 1 Proxmox host with HomeAssistant VM and multiple LXCs
- Separate PC running AdGuard Home
- TerramasterNAS running TrueNAS Scale

**Target Recovery Stack:**
- Proxmox LXC provisioning and configuration
- Media server stack: Radarr, Sonarr, Bazarr, Notifiarr
- Reverse proxy: Nginx Proxy Manager
- HomeAssistant VM restoration

## Architecture and Key Patterns

### Proxmox LXC Management
- Use `proxmox_lxc` role for container provisioning
- Standard LXC templates and configurations
- Automated networking and storage setup
- Container-specific resource allocation

### Media Stack Deployment
- Individual roles for each service: `radarr/`, `sonarr/`, `bazarr/`, `notifiarr/`
- Docker-based deployments within LXCs
- Shared storage mounts for media libraries
- Consistent naming and configuration patterns

### Secret Management
- Uses 1Password CLI for all sensitive data
- Secrets fetched via: `"{{ lookup('community.general.onepassword', 'secret-name') }}"`
- Environment files generated from templates (never committed)
- File permissions set to '0600' for sensitive configs

### Role Development
- Keep roles simple and focused on single services
- Follow standard Ansible role structure
- Use descriptive names matching service names
- Include proper error handling and validation

## Code Standards

### YAML Formatting
- Pre-commit hooks enforce YAML linting, trailing whitespace removal, and end-of-file fixing
- All playbooks must pass `ansible-lint` before merging
- Use consistent indentation and follow YAML best practices

### Naming Conventions
- Playbooks: `deploy_mediastack.yml`, `provision_lxcs.yml` (action-based names)
- Roles: `proxmox_lxc/`, `radarr/`, `sonarr/`, `nginx_proxy_manager/` (service names)
- Variables: `radarr_api_key`, `lxc_memory_size` (snake_case with service prefix)

### CI/CD Integration
- GitHub Actions automatically run `ansible-lint` on all playbooks
- All PRs must pass CI/CD checks before merging
- Use semantic commit messages: `<type>(<scope>): <description>`

## Important Notes

- **Test first**: Always run playbooks in check mode (`--check`) before executing on Proxmox
- **LXC safety**: Verify LXC doesn't exist before provisioning to avoid conflicts
- **Storage mounts**: Ensure NFS/SMB shares from TrueNAS are accessible before media stack deployment
- **Network configuration**: Verify Proxmox bridge and VLAN settings match expected network layout
- **Service dependencies**: Deploy Nginx Proxy Manager before other services that need reverse proxy
- **1Password integration**: Never hardcode API keys, passwords, or tokens - use 1Password CLI lookups
- **Backup configurations**: Store LXC templates and service configurations for easy restoration

## Documentation References

- See `CODE_STANDARDS.md` for detailed coding standards
- See `CONTRIBUTING.md` for PR and contribution guidelines
- See `CHANGELOG.md` for version history and release notes