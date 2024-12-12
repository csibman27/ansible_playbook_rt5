import sys
import subprocess
from pynt import task

@task()
def run_playbook():
    print "running the playbook"
    try:
        subprocess.check_call(["ansible-playbook", "-i", "inventory", "site.yml"]) 
    except subprocess.CalledProcessError:
        raise

@task()
def test():
    print "testing the playbook"
    try:
        subprocess.check_call(["ansible-playbook", "-i", "inventory", "site.yml", "--check"]) 
    except subprocess.CalledProcessError:
        raise

@task()
def get_roles():
    print "fetching the roles from Ansible Galaxy"
    try:
        subprocess.check_call(["ansible-galaxy", "install", "-r", "roles.yml", "-p", "roles", "--force"])
    except subprocess.CalledProcessError:
        raise

@task()
def ping():
    print "pinging..."
    try:
        subprocess.check_call(["ansible", "-i", "inventory", "-m", "ping", "all"])
    except subprocess.CalledProcessError:
        raise

__DEFAULT__ = test
