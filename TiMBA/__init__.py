"""
This is where the main page of the auto generated documentation website can be.

`TIMBA_DATA_DIR` can be either pre-defined and hard coded in the default case,
or it can be defined through an environmental variable.

"""

from pathlib import Path

# Path do the data, default case
TIMBA_DATA_DIR = Path.home() / "timba_data"
# Or defined through an environmental variable
if os.environ.get("TIMBA_DATA_DIR"):
    TIMBA_DATA_DIR = Path(os.environ["TIMBA_DATA_DIR"])

