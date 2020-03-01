#!/usr/bin/env python3

import testinfra.utils.ansible_runner
import os
import re

# https://www.digitalocean.com/community/tutorials/how-to-test-ansible-roles-with-molecule-on-ubuntu-16-04
# https://testinfra.readthedocs.io/en/latest/modules.html#testinfra.modules.file.File
# https://opensource.com/article/19/5/using-testinfra-ansible-verify-server-state
# https://github.com/ansible/molecule/blob/master/test/scenarios/driver/vagrant/molecule/multi-node/tests/test_instance-1.py

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
  os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.exists
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644


def test_package(host):
    assert host.package("ntp").is_installed


def test_file_content(host):
    file = host.file("/etc/mdadm/mdadm.conf")
    pattern = re.compile("\nMAILADDR devops-report@energisme.com")
    assert pattern.search(file.content_string) is not None


def test_service(host):
    if host.system_info.distribution == "debian":
        ntp_daemon = "ntp"
    elif host.system_info.distribution == "centos":
        ntp_daemon = "ntpd"
    else:
        ntp_daemon = "ssh"

    s = host.service(ntp_daemon)
    assert s.is_running
    assert s.is_enabled
