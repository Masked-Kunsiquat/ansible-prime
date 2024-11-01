# Ansible Role: Update & Reboot
This role updates packages on Ubuntu, Debian, and Alpine Linux systems and reboots if necessary.

## Variables

- `update_commands`: OS-specific package update commands for both regular and dist-upgrade.

- `dist_upgrade`: Set to `true` to perform a dist-upgrade (default: `false `).

- `reboot_required`: Set to `true` to reboot if updates were applied (default: `true`).

## Usage
Add this role to your playbook and set variables as needed:

```yaml
- hosts: all
  become: true
  roles:
    - role: update_machines
      vars:
        dist_upgrade: true # Set to `true` for dist upgrade, `false` for standard
```
