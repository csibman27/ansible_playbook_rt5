# Ansible playbook and role for installing rt5

The following is a playbook for test_playbook. 

## How to Use

This is an [Ansible](https://github.com/ansible/ansible) playbook. I've found the best results come from running on a Linux/OSX host.

### Requirements

- A target VM that is tested on Debian 11 with OpenSSH Server installed and running.
- A host with Python, [Pip](https://pypi.python.org/pypi/pip) and [pipenv](http://docs.pipenv.org/en/latest/) installed.
- Full update and upgrade
- Requires apache2 installed
- Requires a preferred database to be installed, recommended is MariaDB MYSQL

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
