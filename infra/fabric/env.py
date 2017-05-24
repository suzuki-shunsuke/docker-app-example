import os

from fabric.api import env
import yaml


AP_ENV = os.environ["AP_ENV"]

with open("servers.yml") as r:
    servers_data = yaml.load(r)

with open("env.yml") as r:
    env_data = yaml.load(r)

env.roledefs = dict(
    (role_name,
     ["{}-{}".format(role_name, idx) for idx in params["vms"].keys()])
    for (role_name, params) in servers_data[AP_ENV].items())

env.update(env_data)
