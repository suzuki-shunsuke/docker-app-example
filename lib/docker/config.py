import os

import yaml


docker_env_path = os.path.join(
    os.path.dirname(__file__), "..", "..", "docker_cfg.yml")

with open(docker_env_path) as r:
    config = yaml.load(r)

dests = {"service": config["services"], "env": config["envs"]}

_a = []
if config["registry"]:
    _a.append(config["registry"])
if config["user"]:
    _a.append(config["user"])
_a.append(config["image"])
image_path = "/".join(_a)
