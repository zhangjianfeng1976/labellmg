import sys
import os

import pytest


def pytest_sessionstart(session):
    """
    Called before performing collection and entering the run test loop.
    """
    CURRENT_FILE_DIR = os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(0, os.path.join(CURRENT_FILE_DIR, '..', 'src'))
    sys.path.insert(0, os.path.join(CURRENT_FILE_DIR, '..', 'src', 'labelImg'))
