## Request Tracker, powered by Ansible
This role provides a means to install BestPractical Request tracker on your system.

It requires:

- Debian 11 with backports enabled or RHEL(-like) 9, the author recommends Debian as more dependencies are packaged
- A MySQL database server already set up
- Internet access (Github, CPAN and distro repos)

If you want to handle e-mail:

- A local MTA configured to deliver e-mail via a smarthost or otherwise
- Either the system itself should be able to receive mail, or you enable ```rt_setup_fetchmail```
  which will install fetchmail and configure to run every few minutes

This role has a soft dependency on using https://github.com/Thulium-Drake/ansible-role-apache_revproxy to provide the webserver. Add the following configuration to your host_vars:

```
apache_apps:
  - name: "{{ ansible_facts['fqdn'] }}"
    type: 'rt5'
    cert: "/etc/ssl/{{ ansible_facts['fqdn'] }}/{{ ansible_facts['fqdn'] }}.crt"
    key: "/etc/ssl/{{ ansible_facts['fqdn'] }}/{{ ansible_facts['fqdn'] }}.key"
    hsts: false
    state: 'present'
```

And this to your requirements:

```
- name: 'apache_revproxy'
  src: 'thulium_drake.apache_revproxy'
```

However, if you have your own means of providing a Apache webserver, you can also use that.
