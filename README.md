# My Ansible Project

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/b73e8e8d98f04af99429c768e24f835a)](https://app.codacy.com/gh/Masked-Kunsiquat/ansible-prime/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

[![CodeFactor](https://www.codefactor.io/repository/github/masked-kunsiquat/ansible-prime/badge)](https://www.codefactor.io/repository/github/masked-kunsiquat/ansible-prime)

This project automates the deployment and recovery of Docker services in a HomeLab environment.

The setup is designed for ease of disaster recovery and overall management by deploying Docker services from scratch on a Proxmox-based infrastructure, with containers organized in LXCs. 

This project uses roles, templates, and variables to streamline the configuration, making it modular and scalable.

## Project Overview

- Goal: Automate the setup and recovery of Docker services, ensuring that all configurations are stored with Ansible to facilitate a qucik rebuild if needed.
- Primary Components:

   - Ansible Roles: Each Docker service is configured as a modular role, allowing services to be added or updated easily.

   - Jinja Templates: Each service has a dedicated `compose.yaml` template stored in the role's template directory.

   - Dynamic Variables: Service directories, environment variables, and configurations are handled with variables - making it adaptable and reusable.

## Directory Structure
```txt
ansible/
├── roles/
│   └── docker_services/
│       ├── tasks/
│       │   └── deploy.yaml # Main tasks file to set up and deploy services
│       ├── templates/
│       │   ├── espocrm-compose.yaml.j2
│       │   ├── radarr-compose.yaml.j2
│       │   ├── sonarr-compose.yaml.j2
│       │   ├── authentik.compose.yaml.j2
│       │   └── ... # Additional service-specific compose templates
│       └── vars/
│           └── main.yaml # Variables for base paths, services, and template path
├── playbooks/
│   ├── deploy_services.yaml # Main playbook to deploy Docker services
│   ├── recovery.yaml # Disaster recovery playbook for redeployment
│   └── network.yaml # Playbook for setting up networking and proxies\
└── inventory/
    └── hosts # Inventory file defining Docker hosts
```

## Key Files and Directories

- `roles/docker_services/vars/main.yaml`: Combines variables for base paths, directories for each services, and the `template_path` variable for dynamic compose.yaml templates.

- `roles/docker_services/templates/`: Stores Jinja templates for each service's compose.yaml, referenced dynamically with the `template_path` variable.

- `roles/docker_services/tasks/deploy.yaml`: Ensures directories exist, creates compose.yaml files from templates, and deploys services using the [docker_compose](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_compose_v2_module.html#ansible-collections-community-docker-docker-compose-v2-module) module.

- `playbooks/deploy_services.yaml`: Main playbook to deploy Docker services across hosts by calling the [docker_services](roles/docker_services/) role.

## Configuration and Usage
### Variables Setup
Variables are defined in [`roles/docker_services/vars/main.yaml`](roles/docker_services/vars/main.yaml) including:

   - `docker_compose_base_path`: The base path where all Docker Compose service directories are stored.

   - `services`: A dictionary defining each service's directory, based on `docker_compose_base_path`.

   - `template_path`: A dynamic path for Jinja templates (e.g. `templates/{{ service }}/compose.yaml.j2`), allowing the role to select the correct template per service.

   Example snippet in `vars/main.yaml`:
   ```yaml
   docker_compose_base_path: "/path/to/docker_compose"
   services:
      espocrm:
         dir: "{{ docker_compose_base_path }}/espocrm"
      radarr:
         dir: "{{ docker_compose_base_path }}/radarr"
      sonarr:
         dir: "{{ docker_compose_base_path }}/sonarr"
      authentik:
         dir: "{{ docker_compose_base_path }}/authentik"
   ```

### Main Task File
The main task file in [`roles/docker_services/tasks/deploy.yaml`](roles/docker_services/tasks/deploy.yaml) dynamically references each service's directory and template, using `service` as a variable for modularity:

```yaml
- name: Esnure {{ service }} directory exists
  file:
    path: " {{ services[service].dir }}"
    state: directory

- name: Generate compose.yaml for {{ service }}
  template:
    src: "{{ template_path }}"
    dest: "{{ services[service].dir }}/compose.yaml"

- name: Deploy {{ service }} using docker_compose
  community.docker.docker_compose:
    project_src: "{{ services[service].dir }}"
    pull: true
    recreate: true
```
## Deploying Services
Run the main playbook [`deploy_services.yaml`](roles/docker_services/playbooks/deploy_services.yaml) to deploy or recover Docker services:
```yaml
- name: Deploy Docker services
  hosts: []
  vars:
    service_list:
      - espocrm
      - radarr
      - sonarr
      - authentik
  roles:
    - docker_services
```
Then execute the playbook:
```bash
ansible-playbook playbooks/deploy_services.yaml -i inventory/hosts
```
## Additional Playbooks

- `recovery.yaml`: Use this playbook for full recovery, deploying all services from scratch on a clean system.

- `network.yaml`: Use this playbook to set up networking and proxies, such as configuring [NGINX Proxy Manager](https://nginxproxymanager.com/).

## Notes

- Modular Design: The structure is designed to be modular, allowing easy addition or modification of services.

- Dynamic Templating: The `template_path` and `services` variables allow the role to adapt to multiple services with minimal configuration.

- Ansible Vault: For sensitive information, it's recommended to use [Ansible Vault](https://docs.ansible.com/ansible/latest/vault_guide/index.html) to securely manage environment variables and other sensitive configurations.
