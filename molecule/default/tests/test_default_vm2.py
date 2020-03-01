#!/usr/bin/env python3

import testinfra.utils.ansible_runner
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('vm2')


def test_package_webserver(host):
    assert host.package("nano").is_installed
    assert host.package("vim").is_installed is False
