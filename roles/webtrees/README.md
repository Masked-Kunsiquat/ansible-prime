# Webtrees Ansible Role

This Ansible role automates the installation and configuration of Webtrees, a web-based genealogy application.

## Requirements

This role assumes you have a Debian-based system with Apache and MySQL/MariaDB already installed. Additionally, ensure that PHP is set up and configured properly for Webtrees.

## Role Variables

The following variables can be customized:

- `php_version`: The major version of PHP to use (default is 7).
- `webtrees_version`: The version of Webtrees to install (default is "2.1.18").
- `webtrees_install_dir`: The directory where Webtrees will be installed (default is "/var/www/webtrees").
- `mysql_database`: The MySQL/MariaDB database name for Webtrees (default is "webtrees_db").
- `mysql_username`: The MySQL/MariaDB username for Webtrees (default is "webtrees_user").
- `mysql_password`: The MySQL/MariaDB password for Webtrees (default is "your_password").
- `mysql_host`: The MySQL/MariaDB host (default is "localhost").

## Dependencies

No dependencies.

## Example Playbook

```yaml
- hosts: servers
  roles:
    - { role: webtrees, php_version: 7, webtrees_version: "2.1.18", mysql_password: "password123" }
