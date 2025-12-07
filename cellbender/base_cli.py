"""Command-line tool functionality.

Parses arguments and determines which tool should be called.

"""

import os
import codecs

# New tools should be added to this list.
TOOL_NAME_LIST = ['remove-background']


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version() -> str:
    return read('VERSION.txt').splitlines()[0]