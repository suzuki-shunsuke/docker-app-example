import os
import sys

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "lib")))

from compile_servers import Compiler  # noqa: E402


def test_get_sshcfg_str():
    pass


def test_get_inventory_str():
    pass


def test_get_conf_path():
    compiler = Compiler()
    assert compiler.get_conf_path() == os.path.abspath("servers.yml")


def test_get_sshcfg_path():
    compiler = Compiler()
    assert compiler.get_sshcfg_path() == os.path.abspath("sshcfg")


def test_get_inventory_path():
    compiler = Compiler()
    assert (compiler.get_inventory_path("dev") ==
            os.path.abspath(os.path.join("inventories", "dev")))


def test_load_yaml():
    compiler = Compiler()
    compiler.load_yaml()


def test_make_sshcfg_str():
    pass


def test_make_inventory_strs():
    pass
