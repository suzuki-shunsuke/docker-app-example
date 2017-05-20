from __future__ import with_statement
from fabric.api import local


def deploy():
    local("whoami")
