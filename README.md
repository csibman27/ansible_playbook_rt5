# Ansible playbook and role for installing rt5

The following is a playbook for test_playbook.

The playbook is tested on Debian 11, Debian 12 

Last Install: 2025-01-15
user: debian
DNS: helpdesk.waltoninstitute.ie
FYI: old helpdesk.tssg.oeg is forwarded to helpdesk.waltoninstitute.ie

## How to Use this playbook

This is an [Ansible](https://github.com/ansible/ansible) playbook. I've found the best results come from running on a Linux/OSX host.

### Requirements

- A target VM that is tested on Debian 11 with OpenSSH Server installed and running.
- A host with Python, [Pip](https://pypi.python.org/pypi/pip) and [pipenv](http://docs.pipenv.org/en/latest/) installed.
- Requires nginx pre installed
- Requires a preferred database to be installed, recommended is MariaDB MYSQL
- https://rt-wiki.bestpractical.com/wiki/ManualInstallation // can provide more info about installation

### RT user

`` 
sudo groupadd --system rt
sudo useradd --system --home-dir=/opt/rt5/var --gid=rt rt
``

### Apache2 config

 
- /etc/apache2/apache2.conf
  ``
  + LoadModule proxy_module /usr/lib/apache2/modules/mod_proxy.so
  + LoadModule proxy_fcgi_module /usr/lib/apache2/modules/mod_proxy_fcgi.so
  ``      
  
- Create a new virtual config in /etc/apache2/sites-enabled/{domain-name}.ie.conf

```
## helpdesk vhost
<VirtualHost *:80>
        ServerName {domain-name}
        ServerAlias helpdesk

        AddDefaultCharset UTF-8

        # ScriptAlias and Location should match RT's WebPath

        # If WebPath is empty then use a single slash:
        ScriptAlias / /opt/rt5/sbin/rt-server.fcgi/
        # If WebPath is 'rt' then add that after the slash:
        # ScriptAlias /rt /opt/rt5/sbin/rt-server.fcgi/

        DocumentRoot "/opt/rt5/share/html"
        ErrorLog /var/log/apache.log
        CustomLog /var/log/apache-access.log combined

        # If WebPath is empty then use a single slash:
        <Location />
        # If WebPath is 'rt' then add that after the slash:
        # <Location /rt>

            Require all granted
            Options +ExecCGI
            AddHandler fcgid-script fcgi
        </Location>

</VirtualHost>

```

- Debian 

  * sudo a2dismod mpm_event
  * sudo a2dismod mpm_worker
  * sudo a2enmod mpm_prefork
  * sudo a2enmod fcgid
  * systemctl restart apache2

### Install DB

+ sudo apt update
+ sudo apt install mariadb-server
+ sudo mysql_secure_installation

+ sudo mysql -u root -p

+ You do not need to create db and user manually RT will do it for you;
+ GRANT ALL PRIVILEGES ON rt.* TO rt@localhost IDENTIFIED BY 'YourPassphraseHere' WITH GRANT OPTION;

### How to run RT5 first time

1. Double check initial config and credentials in /opt/rt5/etc/RT_SiteConfig.pm
   - Sytax check ``perl -c /opt/rt5/etc/RT_SiteConfig.pm``
1. Create a database user "rt"
   - Add required db permissions for the user
   - ``GRANT ALL PRIVILEGES ON rt.* TO rt@localhost IDENTIFIED BY 'YourPassphraseHere' WITH GRANT OPTION;``
1. Initialize the database
   - ``sudo /opt/rt5/sbin/rt-setup-database --action=init``
   - This will initialize the database and creates indexes required 
1. Full text search is disabled in your RT configuration and it needs to be enabled
   - ``sudo /opt/rt5/sbin/rt-setup-fulltext-index``
1. **AT THIS STAGE YOU HAVE RT RUNNING! MAKE SURE YOU CAN CONFIRM THAT, ELSE GO BACK IN DOCS**
1. RT’s root user password can be changed with the commnad
   - ``sudo /opt/rt5/sbin/rt-passwd root``
1. Login to RT without any SSL cert required the following code in place  `` Set($WebSecureCookies, 0); `` to RT_SiteConfig
1. The application can be run number of ways
   1. Apache: FCGI (this is the recommended way and all explained above)
   1. Nginx: <https://rt-wiki.bestpractical.com/wiki/ManualInstallation>
   1. Standalone with extension: The application can be run with starman, that would require an extra package to install
      - `` cpanm --sudo Plack::Handler::Starman ``
      - `` sudo /opt/rt5/sbin/rt-server --server Starman --port 5000 ``
   1. Standalone without any extension:
      - `` sudo /opt/rt5/sbin/rt-server --port 5000 ``
1. Any permission issues make sure var directory has correct owner set.
      - `` sudo chown -R www-data:rt /opt/rt5/var ``
1. ROOT login - reset password /opt/rt5/sbin/rt-passwd root

### Test Emails internaly

- Install postfix, make sure transport and virtual files exist after removed sendmail
- Incoming from localhost
  * echo 'hello' | mail -s "whassup" rt

### Plugins could be added

- https://github.com/medea61/RT-Extension-MSTeams

### Method

This is an ansible playbook that contains the role so run it with the ansible command provided in run.txt
Edit the inventory; adding the hostname or IP address of the target VM.
Edit 'ansible.cfg' making sure you're happy with the remote user and authentication method (password, key, etc.).


This runs the playbook with the inventory and the ansible configuration.

## Contribution

Tibor Molnar tibor.molnar@waltoninstitute.ie

# ansible_playbook_rt5
