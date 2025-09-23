# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a modular Ansible repository designed for **flexible homelab infrastructure management**. The primary goal is to provide composable, idempotent roles that can deploy services across different platforms (LXCs, Docker hosts, bare metal) based on service requirements and personal preferences.

## Architecture Philosophy

### Modular Design
- **Composable roles**: Each role does one thing well and can be combined with others
- **Platform flexibility**: Services can run in LXCs, Docker containers, or bare metal as appropriate
- **True idempotency**: All playbooks can be run repeatedly without issues
- **Predictable structure**: Consistent patterns across all deployments

### Platform Strategy
- **LXCs**: For services that benefit from isolation, easy backup, or small footprint
- **Docker**: For services with good containerization support
- **Bare metal**: For services that require direct hardware access
- **Choice by service**: Platform selection based on service needs and preferences

## Development Commands

### Linting and Testing
```bash
# Install pre-commit hooks (required for development)
pip install pre-commit
pre-commit install

# Lint Ansible playbooks and roles
ansible-lint roles/ playbooks/

# Test individual roles in check mode
ansible-playbook -i inventory/hosts playbooks/test-role.yml --check --extra-vars "target_role=docker_host"

# Run with verbose output for debugging
ansible-playbook -i inventory/hosts playbooks/main.yml -vv
```

### Role Testing
```bash
# Test a specific role
ansible-playbook -i inventory/hosts playbooks/deploy-service.yml --tags "sonarr" --check

# Deploy single service
ansible-playbook -i inventory/hosts playbooks/deploy-service.yml --extra-vars "service=nginx_proxy_manager platform=lxc"
```

## Repository Structure

```
├── inventory/
│   ├── hosts                    # Server inventory
│   ├── group_vars/             # Group-specific variables
│   └── host_vars/              # Host-specific variables
├── roles/
│   ├── infrastructure/         # Platform provisioning roles
│   │   ├── proxmox_lxc/       # LXC provisioning
│   │   ├── docker_host/       # Docker host setup
│   │   └── common/            # Common OS configuration
│   ├── services/              # Individual service roles
│   │   ├── sonarr/           # Sonarr deployment (Docker)
│   │   ├── nginx_proxy_manager/ # NPM deployment
│   │   └── home_assistant/    # Home Assistant (LXC)
├── playbooks/
│   ├── main.yml              # Main orchestration playbook
│   ├── deploy-service.yml    # Single service deployment
│   └── provision-platform.yml # Platform provisioning
├── templates/
│   ├── docker/               # Docker compose templates
│   └── systemd/              # Systemd service templates
└── group_vars/
    ├── docker_hosts.yml      # Docker host configuration
    └── proxmox.yml          # Proxmox configuration
```

## Role Architecture

### Infrastructure Roles
- **proxmox_lxc**: Creates and configures LXC containers
- **docker_host**: Sets up Docker daemon and directory structure
- **common**: Base OS configuration (users, packages, security)

### Service Roles
- Each service gets its own role (sonarr, radarr, nginx_proxy_manager, etc.)
- Service roles are platform-agnostic where possible
- Role determines deployment method based on `platform` variable

### Role Interaction Pattern
```yaml
# Example: Deploy Sonarr in LXC
- include_role: name=proxmox_lxc
  vars:
    lxc_name: sonarr
    lxc_vmid: 201
- include_role: name=sonarr
  vars:
    platform: lxc
    target_host: "{{ lxc_name }}"
```

## Docker Structure Standards

### Directory Layout
```
/docker/
├── sonarr/
│   ├── compose.yaml
│   ├── .env
│   └── data/
├── radarr/
│   ├── compose.yaml
│   ├── .env
│   └── data/
└── nginx-proxy-manager/
    ├── compose.yaml
    ├── .env
    └── data/
```

### File Standards
- **compose.yaml**: Docker Compose file (generated from Jinja template)
- **.env**: Environment variables (generated from Jinja template, mode 0600)
- **data/**: Service data directory

## Secret Management with 1Password

### Organization Structure
- **Vault**: "HomeLab" (dedicated vault for homelab secrets)
- **Item Structure**: One item per service with multiple fields (e.g., `sonarr` item with `api_key`, `db_password` fields)
- **Lookup Pattern**: `"{{ lookup('community.general.onepassword', 'service-name', field='field_name', vault='HomeLab') }}"`

### Template Integration
```yaml
# In Jinja templates - single item with multiple fields
SONARR_API_KEY={{ lookup('community.general.onepassword', 'sonarr', field='api_key', vault=onepassword_vault) }}
DB_PASSWORD={{ lookup('community.general.onepassword', 'sonarr', field='db_password', vault=onepassword_vault) }}

# For services with multiple instances, use item_name override:
API_KEY={{ lookup('community.general.onepassword', config.item_name | default('sonarr'), field='api_key', vault=onepassword_vault) }}
```

### 1Password Item Standards
- **Item name**: Match service name (lowercase, hyphenated: `nginx-proxy-manager`, `ddns-updater`)
- **Field names**: Descriptive, lowercase with underscores (`api_key`, `db_password`, `zone_id`)
- **Multiple instances**: Create separate items (`sonarr-4k`, `radarr-anime`) or use `item_name` parameter

## Service Deployment Patterns

### Docker Service Role Structure
```
roles/sonarr/
├── tasks/main.yml           # Main deployment logic
├── templates/
│   ├── compose.yaml.j2      # Docker compose template
│   └── .env.j2             # Environment template
├── defaults/main.yml        # Default variables
└── vars/main.yml           # Service-specific variables
```

### LXC Service Deployment
```yaml
- name: Create LXC for service
  include_role:
    name: proxmox_lxc
  vars:
    lxc_name: "{{ service_name }}"
    lxc_vmid: "{{ service_vmid }}"

- name: Deploy service in LXC
  include_role:
    name: "{{ service_name }}"
  vars:
    platform: lxc
    ansible_host: "{{ lxc_ip }}"
```

## Key Principles

### Idempotency
- All roles must be safe to run multiple times
- Use `creates` parameter for one-time operations
- Check service state before making changes

### Modularity
- Each role has a single responsibility
- Roles communicate through well-defined variables
- Platform-specific logic contained within roles

### Flexibility
- Service roles work across platforms (LXC, Docker, bare metal)
- Configuration driven by variables and templates
- Easy to add new services or platforms

### Secret Management Standards
- **One item per service**: Each service gets a single 1Password item (e.g., `sonarr`, `ddns-updater`)
- **Multiple fields per item**: Store related secrets as fields within the service item
- **Consistent naming**: Item names match service names, field names use underscores
- **Template consistency**: Always use `lookup('community.general.onepassword', 'service-name', field='field_name', vault=onepassword_vault)`

## Important Notes

- **Test first**: Always use `--check` mode for new deployments
- **One service per role**: Keep roles focused on single services
- **Template everything**: Use Jinja2 for all configuration files
- **Secret security**: Never hardcode secrets, always use 1Password lookups
- **Directory standards**: Follow `/docker/{service}/compose.yaml` pattern
- **File permissions**: Set `.env` files to mode 0600
- **Platform choice**: Choose platform based on service needs, not convenience