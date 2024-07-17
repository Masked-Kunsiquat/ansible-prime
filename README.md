# My Ansible Project

This project contains Ansible playbooks and roles to set up and configure various components in a HomeLab environment. The roles are designed to be modular and support multiple Linux distributions, including Ubuntu, Debian, and Alpine Linux.

## Table of Contents

- [Setup Machine Role](roles/setup_machine/README.md)
- [SuiteCRM Role](roles/suitecrm/README.md)
- [MySQL Role](roles/mysql/README.md)

## Getting Started

### Prerequisites

- Ansible installed on your control machine
- SSH access to the target machines

### Directory Structure


### Running Playbooks

1. **Setup Machine Playbook**:
   ```sh
   ansible-playbook -i hosts setup_machine_playbook.yml

2. **Install SuiteCRM Playbook**:
    ```sh
    ansible-playbook -i hosts install_suitecrm_playbook.yml
