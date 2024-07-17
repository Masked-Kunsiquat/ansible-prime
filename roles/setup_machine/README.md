# Setup Machine Role

This role sets up a machine by creating a user, configuring SSH, and installing necessary packages. It supports multiple Linux distributions, including Ubuntu, Debian, and Alpine Linux.

## Variables

- `setup_machine_new_user`: The username of the new user to be created (default: `myuser`)
- `setup_machine_user_password`: The password for the new user (default: `password`)
- `setup_machine_ssh_key_path`: Path to the SSH public key for the new user (default: `''`)
- `setup_machine_packages_common`: List of common packages to install on all distributions
- `setup_machine_packages_debian`: List of packages to install on Debian/Ubuntu
- `setup_machine_packages_alpine`: List of packages to install on Alpine
- `setup_machine_file_owner`: The owner of files and directories created by the role (default: `setup_machine_new_user`)
- `setup_machine_file_group`: The group of files and directories created by the role (default: `setup_machine_new_user`)

## Usage

Include this role in your playbook:

```yaml
- hosts: homelab
  become: yes
  vars:
    setup_machine_new_user: 'custom_user'
    setup_machine_user_password: 'custom_password'
    setup_machine_ssh_key_path: ''  # Leave this empty if not passing an SSH key
    setup_machine_packages_common:
      - git
      - curl
      - vim
    setup_machine_packages_debian:
      - htop
      - tree
    setup_machine_packages_alpine:
      - htop
      - tree
    setup_machine_file_owner: 'custom_user'
    setup_machine_file_group: 'custom_user'
  roles:
    - setup_machine
