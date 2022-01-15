import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_java_package_exists(host):
    cmd = host.run("mcrcon -v")
    assert cmd.rc == 0

