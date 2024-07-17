# MySQL Role

This role installs and configures MySQL/MariaDB. It supports multiple Linux distributions, including Ubuntu, Debian, and Alpine Linux.

## Variables

- `db_root_password`: MySQL root password
- `db_name`: Database name to create
- `db_user`: Database user to create
- `db_password`: Database user password
- `mysql_file_owner`: Owner of the MySQL files (default: `mysql`)
- `mysql_file_group`: Group of the MySQL files (default: `mysql`)

## Usage

Include this role in your playbook:

```yaml
- hosts: homelab
  become: yes
  vars:
    db_root_password: 'root_password'
    db_name: 'suitecrm'
    db_user: 'suitecrm_user'
    db_password: 'suitecrm_password'
  roles:
    - mysql
