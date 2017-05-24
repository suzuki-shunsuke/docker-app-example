#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import yaml


class Compiler(object):
    def get_sshcfg_str(self, **kwargs):
        return "\n".join([
            "Host {type}-{idx}.{env}",
            "  HostName {ip}",
            "  User {user}",
            "  IdentityFile ssh-keys/{type}.{env}",
            "  UserKnownHostsFile ssh-keys/known_hosts",
        ]).format(**kwargs)

    def get_inventory_str(self, **kwargs):
        type_ = kwargs["type"]
        env = kwargs["env"]
        results = ["[{type}]".format(type=type_)]
        for idx in kwargs["idxs"]:
            results.append("{type}-{idx}.{env}".format(
                idx=idx, type=type_, env=env))
        return "\n".join(results)

    def get_conf_path(self):
        return os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..", "servers.yml"))

    def get_sshcfg_path(self):
        return os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..", "sshcfg"))

    def get_inventory_path(self, env):
        return os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..", "inventories", env))

    def load_yaml(self):
        with open(self.get_conf_path()) as r:
            return yaml.load(r)

    def make_sshcfg_str(self, data):
        results = ["# vi: set ft=sshconfig :"]
        for env, env_data in data.items():
            for type_, type_data in env_data.items():
                for idx, vm_data in type_data["vms"].items():
                    results.append(self.get_sshcfg_str(
                        env=env, idx=idx, type=type_, ip=vm_data["ip"],
                        user=type_data["params"]["user"]))
        return "\n".join(results)

    def make_inventory_strs(self, data):
        return dict((env, "\n\n".join(self.get_inventory_str(
            type=type_, env=env, idxs=type_data["vms"].keys())
            for type_, type_data in env_data.items()))
            for env, env_data in data.items())

    def write_sshcfg(self, data):
        with open(self.get_sshcfg_path(), "w") as w:
            w.write(self.make_sshcfg_str(data))

    def write_inventories(self, data):
        for env, txt in self.make_inventory_strs(data).items():
            with open(self.get_inventory_path(env), "w") as w:
                w.write(txt)
