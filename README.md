# Common tools to install to all servers**

## Purpose

This project solves server environment configuration issues. One servers are grouped by types, packages, files, file modification can be managed using variable file configuration.
Making every servers of the same type ISO.

## How to use

The entrypoint of this ansible project is the configuration file (`molecule/default/var.yml`). Tasks load configuration and setup remote server according to it. Each variable in the configuration file match to one Ansible task.

For example, the `commontools_packages_install` variable describes packages that will be added on every targeted servers. This variable matches to `task/package/install_packages.yml` Ansible task.

Then `commontools_packages_install_extra` variable describes packages that will be added on servers depending of its group defined in `molecule/default/inventory.yml`. Condition is implemented using When and multi-dimensional Loop instructions.
This variable matches to `task/package/install_extra_packages.yml` Ansible task.

## Example

A playbook example using this role can be found at `molecule/default/playbook.yml`.
Configuration (variable file) at `molecule/default/var.yml`.

## CI requirement

In order to runner CI pipeline properly, the runner attached must have privileges and use `/var/run/docker.sock:/var/run/docker.sock` as volume.

## Prerequisit

Load GitLab ssh keys in ssh-agent for downloading ansible Energisme roles.
