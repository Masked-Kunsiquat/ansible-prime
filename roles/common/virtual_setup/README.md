# virtual_setup Ansible Role

The `virtual_setup` Ansible role sets up common configurations for virtual servers, including SSH configurations and user management.

## Requirements

This role assumes you have a Debian-based system.

## Role Variables

The following variables can be customized:

- `newadmin_username`: The username of the new admin (default is "serveradmin").
- `newadmin_base_directory`: The base directory for the new admin (default is "/home/{{ newadmin_username }}").
- `newadmin_passwd_directory`: The directory to store the admin's password (default is "{{ newadmin_base_directory }}/.passwd").
- `newadmin_password_file`: The file to store the admin's password (default is "{{ newadmin_passwd_directory }}/pass.txt").
- `newadmin_ssh_pub_key`: The SSH public key for the admin (default is "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC+PpHslH0sr9pmkLMU3CRfZfNbHoDprS3sly8L4MFHxhP7D14ylrJ31omY1qwXPKD1CjJGrQSkStQKwu15M0Yt3hPKEEebVj1PlOuGJct9L2CGk0SyYl0Hv7X8+RrOUQogJh0tHUJQUkYXpvPndS1xekn4EM3qCVJ+n2CsyZM+74jFZ9Fcl9IcRX7BZsm1eBvGfKxxTDZlzO2qOChJyjzOsDP96zS7yVXtxA4GCR3WiJjI+w5nJvcUrf8mtj8AyRRH0p4/yI5AXJwP7c4D5v8aH0Hp4q/0b6j1uBcaGOL1elJ55BrWpR08B0/kUJ6Mvw1xF9NRwMuWbN9+hSKucTWW5vVSHaYmJ4z0ZBFKnxYnBQhzWZmTCXG4pB2QSCf3sMQgZlNf/Ew2E4xVRjAwhx4rhNT0KLsV7X5DfyoY7OjDp7uFyTZ3jbzv4iXSGCVsDsHnAs49t2XyVbd8YVmoxY+QuHccY/4N/IdQQJW/F5QD1e2BYLAEzjYoDe88PUPGNq5sWZXNQcbQCKjt+xqEKRX5EhzAMqXZ6+2eB/CUkjpUzr4GqK6rNFwJu4q0jQaA7oyg6zv+PZiWlLACmdBhRcQdEOnhv0n69Oz1SNblMk5oGfo3tqHmBdF8UG8Q3QmCmKOCvG6jLxGtYw== user@example.com").
- `additional_ssh_keys`: Additional SSH public keys to add (default is an empty list).

## Dependencies

No dependencies.

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: virtual_setup
      newadmin_username: serveradmin
      newadmin_password_file: "/home/serveradmin/.passwd/pass.txt"
      newadmin_ssh_pub_key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
      additional_ssh_keys:
        - "{{ lookup('file', '~/.ssh/authorized_keys') }}"

