# Ansible playbook and role for installing rt5

The following is a playbook for test_playbook.

The playbook is tested on Debian 11, Debian 12 

## How to Use

This is an [Ansible](https://github.com/ansible/ansible) playbook. I've found the best results come from running on a Linux/OSX host.

### Requirements

- A target VM that is tested on Debian 11 with OpenSSH Server installed and running.
- A host with Python, [Pip](https://pypi.python.org/pypi/pip) and [pipenv](http://docs.pipenv.org/en/latest/) installed.
- Requires apache2 pre installed
- Requires a preferred database to be installed, recommended is MariaDB MYSQL
- https://rt-wiki.bestpractical.com/wiki/ManualInstallation // can provide more info about installation

### Apache install & config

- Debian 
  * sudo apt install apache2 libapache2-mod-fcgid
  * sudo a2dismod mpm_event
  * sudo a2dismod mpm_worker
  * sudo systemctl restart apache2
  * sudo a2enmod mpm_prefork
  * sudo systemctl restart apache2
  
- Red Hat/Fedora/CentOS
  * sudo dnf install httpd
  
- Create a new virtual config in /etc/apache2/sites-enabled/<your_domain_name.ie.conf> and
add below code as content.

```
<VirtualHost *:80>
    ServerName www.example.com
    ServerAlias example.com

    ### Optional apache logs for RT
    # Ensure that your log rotation scripts know about these files
    # ErrorLog /opt/rt5/var/log/apache2.error
    # TransferLog /opt/rt5/var/log/apache2.access
    # LogLevel debug

    AddDefaultCharset UTF-8

    # ScriptAlias and Location should match RT's WebPath

    # If WebPath is empty then use a single slash:
    ScriptAlias / /opt/rt5/sbin/rt-server.fcgi/
    # If WebPath is 'rt' then add that after the slash:
    # ScriptAlias /rt /opt/rt5/sbin/rt-server.fcgi/

    DocumentRoot "/opt/rt5/share/html"

    # If WebPath is empty then use a single slash:
    <Location />
    Allow from all

    Require all granted
    Options +ExecCGI
    AddHandler fcgid-script fcgi
    </Location>


    <Directory /opt/rt5/share/html>
        Options -Indexes +FollowSymLinks
        AllowOverride All
    </Directory>

    ErrorLog /var/log/example.com-error.log
    CustomLog /var/log/example.com-access.log combined
</VirtualHost>

```

### Run

- After playbook is done
  * Goto /opt/rt5 and run ***'sudo sbin/rt-setup-database --action=init'*** // this will initialize the database and creates user defined in RT_SiteConfig.pm
- Full text search is disabled in your RT configuration.  Run ***"sudo /opt/rt5/sbin/rt-setup-fulltext-index" to enable it.***
- The application can be run with starman, that would require an extra package to install
- `` cpanm --sudo Plack::Handler::Starman ``
- Command to run the newly installed rt5
- `` sudo /opt/rt5/sbin/rt-server --server Starman --port 5000 ``

### Method

This is a playbook that contains the role so run it with the ansible command provided in run.txt
Edit the inventory; adding the hostname or IP address of the target VM.
Edit 'ansible.cfg' making sure you're happy with the remote user and authentication method (password, key, etc.).


This runs the playbook with the inventory and the ansible configuration.

## Contribution

- Don't bother

Tibor Molnar tibor.molnar@waltoninstitute.ie

&copy; Waterford Institute of Technology 2021-07-23 
# ansible_playbook_rt5
