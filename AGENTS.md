# AGENTS.md

This file defines simple, focused AI agents for homelab disaster recovery automation. Each agent handles specific aspects of rebuilding your homelab infrastructure.

## Available Agents

### proxmox-manager
**Purpose**: Handles Proxmox LXC provisioning and VM management
**Use Cases**:
- Create and configure LXCs with proper resource allocation
- Set up networking and storage for containers
- Manage LXC templates and base configurations
- Handle HomeAssistant VM provisioning and restoration
- Configure Proxmox host networking and storage mounts

### mediastack-deployer
**Purpose**: Deploys and configures media server applications
**Use Cases**:
- Deploy Radarr, Sonarr, Bazarr, and Notifiarr in LXCs
- Configure Docker Compose setups for media services
- Set up shared storage mounts from TrueNAS
- Handle service-to-service communication and API keys
- Configure Nginx Proxy Manager for reverse proxy

### homelab-validator
**Purpose**: Tests and validates homelab deployments
**Use Cases**:
- Run ansible-lint on all playbooks before deployment
- Test LXC connectivity and service health
- Validate storage mounts and network connectivity
- Check service configurations and 1Password integrations
- Perform dry-runs before actual deployment

## Agent Usage Patterns

### Full Disaster Recovery
1. **proxmox-manager**: Provision all LXCs and restore HomeAssistant VM
2. **mediastack-deployer**: Deploy all media services with proper configurations
3. **homelab-validator**: Verify everything is working correctly

### Adding New Services
1. **proxmox-manager**: Create new LXC for the service
2. **mediastack-deployer**: Deploy and configure the new service
3. **homelab-validator**: Test the new deployment

### Maintenance and Updates
1. **homelab-validator**: Test configurations before changes
2. **mediastack-deployer**: Update service configurations
3. **homelab-validator**: Verify updates were successful

## Key Capabilities

### Infrastructure Focus
- **Proxmox LXC Management**: Template-based container creation with standard resource allocation
- **Storage Integration**: Automated NFS/SMB mount setup from TrueNAS
- **Network Configuration**: VLAN and bridge setup for proper network isolation
- **Service Dependencies**: Ensure proper deployment order (Nginx Proxy Manager first)

### Media Stack Specialization
- **Docker Integration**: Standardized Docker Compose deployments within LXCs
- **Configuration Templates**: Jinja2 templates for service configs with 1Password integration
- **API Key Management**: Secure handling of service-to-service API keys
- **Storage Mapping**: Consistent media library paths across all services

### Validation and Safety
- **Pre-deployment Checks**: Verify prerequisites before deployment
- **Health Monitoring**: Post-deployment service validation
- **Rollback Capability**: Safe rollback procedures for failed deployments
- **Documentation**: Maintain simple deployment logs and configurations

## Simple Usage Guidelines

- Use **proxmox-manager** when working with containers or VMs
- Use **mediastack-deployer** when configuring media services
- Always use **homelab-validator** before and after major changes
- Keep it simple - these agents should make disaster recovery straightforward, not complicated