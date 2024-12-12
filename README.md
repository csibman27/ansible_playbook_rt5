# test_playbook

The following is a playbook for test_playbook. 

## How to Use

This is an [Ansible](https://github.com/ansible/ansible) playbook. I've found the best results come from running on a Linux/OSX host.

### Requirements

- A target VM with OpenSSH Server installed and running.
- A host with Python, [Pip](https://pypi.python.org/pypi/pip) and [pipenv](http://docs.pipenv.org/en/latest/) installed.

### Method

Fork/clone this repository.

In the repository directory:

    $ pipenv install --dev
    $ pipenv shell
    $ pynt get_roles

Edit the inventory; adding the hostname or IP address of the target VM.
Edit 'ansible.cfg' making sure you're happy with the remote user and authentication method (password, key, etc.).

    $ pynt

This runs the playbook with the inventory and the ansible configuration.

## Contribution

- Post an issue to the [issue tracker](/../issues/new)
- Fork the repo, make some changes and submit a [Merge Request](/../merge_requests/new)
- Patches, docs, tutorials and feedback are all welcome.

Tibor Molnar tmolnar@tssg.org

&copy; Waterford Institute of Technology 2021-07-23 
# ansible_playbook_rt5
