"""
If the package was using a tool such as pdoc or sphynx to generate the
documentation automatically from docstrings, this is where the main page of the
documentation would be.

`TIMBA_DATA_DIR` can be either pre-defined and hard coded in the default case,
or it can be defined through an environmental variable.

Start python in the TiMBA environment

    cd TiMBA
    source .venv/bin/activate
    ipython

Display the location of the data `TIMBA_DATA_DIR` at a python console:

    >>> from TiMBA import TIMBA_DATA_DIR
    >>> print(TIMBA_DATA_DIR)

"""
import os
import sys
from pathlib import Path


INIT_FILE = sys.modules[__name__].__file__
PACKAGE_DIR = Path(INIT_FILE).parent

# Default path to the data
# See caveats of storing the data inside the package in issue ...
TIMBA_DATA_DIR = PACKAGE_DIR / "data"

# Path to the data defined through an environmental variable
if os.environ.get("TIMBA_DATA_DIR"):
    TIMBA_DATA_DIR = Path(os.environ["TIMBA_DATA_DIR"])
