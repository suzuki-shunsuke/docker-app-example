import os
import sys


REPO_ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
sys.path.append(REPO_ROOT)

from lib.argp import VariableDestAction
from lib.docker.config import dests, image_path, config as cfg

sys.path.pop()
