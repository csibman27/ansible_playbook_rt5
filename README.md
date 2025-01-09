# Ansible playbook and role for installing rt5

The following is a playbook for test_playbook.

The playbook is tested on Debian 11, Debian 12 

## How to Use

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

### Nginx install & config

- Debian 
  * sudo apt install nginx
  * sudo apt-get install spawn-fcgi 
  
- Create a new virtual config in /etc/nginx/sites-available/<your_domain_name.ie> and
add below code as content or use default

```
server {
	listen 80 default_server;
	listen [::]:80 default_server;

        root /opt/rt5/share/html;
       
        access_log  /var/log/nginx/access.log;

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name helpdesk.waltoninstitute.ie;

        # The location path should match the WebPath in your RT site configuration.
        location / {
          include /etc/nginx/fastcgi.conf;
          # SCRIPT_NAME should match RT's WebPath, without a trailing slash.
          # This means when WebPath is /, it's the empty string "".
          fastcgi_param SCRIPT_NAME "";
          # This network location should match the ListenStream in rt-server.socket.
          fastcgi_pass localhost:5000;
        }
}

```

### How to run RT5

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
1. RT’s root user password can be changed with the commnad
   - ``sudo /opt/rt5/sbin/rt-passwd root``
1. If you want to login to RT without any SSL cert in place you have to add `` Set($WebSecureCookies, 0); `` to RT_SiteConfig
1. The application can be run with starman, that would require an extra package to install
   - `` cpanm --sudo Plack::Handler::Starman ``
1. Commands to run the newly installed rt5 (no need apache or nginx)
   - `` sudo /opt/rt5/sbin/rt-server --server Starman --port 5000 `` or without starman
   - `` sudo /opt/rt5/sbin/rt-server --port 5000 ``

### Method

This is an ansible playbook that contains the role so run it with the ansible command provided in run.txt
Edit the inventory; adding the hostname or IP address of the target VM.
Edit 'ansible.cfg' making sure you're happy with the remote user and authentication method (password, key, etc.).


This runs the playbook with the inventory and the ansible configuration.

## Contribution

Tibor Molnar tibor.molnar@waltoninstitute.ie

# ansible_playbook_rt5
