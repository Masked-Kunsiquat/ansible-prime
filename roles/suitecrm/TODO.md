## SuiteCRM Ansible Role To-Do List

~~1. **Configure PHP Settings:**~~
   ~~- Update `php.ini` files:~~
     ~~- `/etc/php/8.1/cli/php.ini`~~
     ~~- `/etc/php/8.1/apache2/php.ini`~~
   ~~- Set:~~
     ~~- `upload_max_filesize = 6M`~~
     ~~- `post_max_size = 6M`~~

~~2. **Ensure Required PHP Packages are Installed:**~~
  ~~- Install necessary PHP packages:~~
     ~~- `php8.1-cli`, `php8.1-fpm`, `php8.1-mysql`, `php8.1-curl`, `php8.1-xml`, `php8.1-mbstring`, `php8.1-zip`, `php8.1-gd`, `php8.1-imap`, `php8.1-intl`, `php8.1-soap`~~

3. **Reset Permissions After Running CLI Installer:**
   - Adjust permissions for SuiteCRM files and directories:
     ```bash
     find . -type d -not -perm 2755 -exec chmod 2755 {} \;
     find . -type f -not -perm 0644 -exec chmod 0644 {} \;
     find . ! -user www-data -exec chown www-data:www-data {} \;
     chmod +x bin/console
     ```

~~4. **Use Placeholders in `defaults/main.yaml`:**~~
    ~~- Implement placeholders for sensitive data and use playbook variables:~~
    ~~- Ensure variables are set in the playbook to avoid leaking secrets on GitHub or other platforms.~~

5. **Testing and Validation:**
   - Test the Ansible role thoroughly to verify correct configuration and installation of SuiteCRM.
   - Validate functionality across different environments to ensure consistency.

6. **Documentation and Maintenance:**
   - Document steps clearly within the Ansible role's documentation (`README.md` or similar).
   - Include specific instructions and dependencies relevant to your SuiteCRM deployment.

