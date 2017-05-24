#!/usr/bin/env python

"""
/lib/docker/build.py
"""

import argparse
import subprocess
import sys


description = "description"
ARGS_HELP = """
""".strip()


def get_parser(**kwargs):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "env", dests=dests, default=kwargs.get("env"),
        action=VariableDestAction)
    parser.add_argument(
        "service", dests=dests, default=kwargs.get("service"),
        action=VariableDestAction)
    return parser


def get_dockerfile_path():
    pass


def get_image_path():
    pass


def get_tag():
    pass


def get_context_path():
    return "."


def cmd(service, env):
    if service:
        if env:
            image = "{}.{}:{}-*".format(image_path, service, env)
        else:
            image = "{}.{}:*".format(image_path, service)
    else:
        if env:
            image = "{}.*:{}-*".format(image_path, env)
        else:
            image = "{}.*".format(image_path)
    args = ["docker", "-f", "", "build", "-t", image, ""]
    cmd_str = " ".join(args)
    L = len(cmd_str)
    deco = "=" * L
    sys.stdout.write("{}\n{}\n{}\n".format(deco, cmd_str, deco))
    p = subprocess.Popen(args)
    return p.wait()


def main():
    parser = get_parser()
    args = parser.parse_args()
    sys.exit(cmd(args.service, args.env))


if __name__ == "__main__":
    main()
