# SuiteCRM Role

This role installs and configures SuiteCRM along with its necessary dependencies. It supports multiple PHP versions to match the SuiteCRM compatibility matrix.

## Variables

- `suitecrm_version`: The version of SuiteCRM to install (default: `7.11.18`)
- `suitecrm_url`: URL to download the SuiteCRM package
- `suitecrm_install_dir`: Directory where SuiteCRM will be installed
- `suitecrm_db_root_password`: MySQL root password
- `suitecrm_db_name`: Database name for SuiteCRM
- `suitecrm_db_user`: Database user for SuiteCRM
- `suitecrm_db_password`: Database password for SuiteCRM
- `suitecrm_php_version`: PHP version to install
- `suitecrm_file_owner`: Owner of the SuiteCRM files (default: `www-data`)
- `suitecrm_file_group`: Group of the SuiteCRM files (default: `www-data`)

## Usage

Include this role in your playbook:

```yaml
- hosts: homelab
  become: yes
  vars:
    suitecrm_version: '7.11.18'
    suitecrm_url: "https://suitecrm.com/files/162/SuiteCRM-{{ suitecrm_version }}/release/413/SuiteCRM-{{ suitecrm_version }}.zip"
    suitecrm_install_dir: /var/www/html/suitecrm
    suitecrm_db_root_password: 'root_password'
    suitecrm_db_name: 'suitecrm'
    suitecrm_db_user: 'suitecrm_user'
    suitecrm_db_password: 'suitecrm_password'
    suitecrm_php_version: '7.4'
    suitecrm_file_owner: 'www-data'
    suitecrm_file_group: 'www-data'
  roles:
    - role: mysql
      vars:
        mysql_db_root_password: "{{ suitecrm_db_root_password }}"
        mysql_db_name: "{{ suitecrm_db_name }}"
        mysql_db_user: "{{ suitecrm_db_user }}"
        mysql_db_password: "{{ suitecrm_db_password }}"
    - suitecrm
