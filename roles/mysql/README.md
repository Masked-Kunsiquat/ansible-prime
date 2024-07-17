# MySQL Role

This role installs and configures MySQL/MariaDB. It supports multiple Linux distributions, including Ubuntu, Debian, and Alpine Linux.

## Variables

- `mysql_db_root_password`: MySQL root password
- `mysql_db_name`: Database name to create
- `mysql_db_user`: Database user to create
- `mysql_db_password`: Database user password
- `mysql_file_owner`: Owner of the MySQL files (default: `mysql`)
- `mysql_file_group`: Group of the MySQL files (default: `mysql`)

## Usage

Include this role in your playbook:

```yaml
- hosts: homelab
  become: yes
  vars:
    mysql_db_root_password: 'root_password'
    mysql_db_name: 'suitecrm'
    mysql_db_user: 'suitecrm_user'
    mysql_db_password: 'suitecrm_password'
  roles:
    - mysql
