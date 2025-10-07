import datetime as dt
from TiMBA import TIMBA_DATA_DIR

current_dt = dt.datetime.now().strftime("%Y%m%dT%H-%M-%S")

# input
INPUT_WORLD_PATH = TIMBA_DATA_DIR / "input/01_Input_Files/"
ADDITIONAL_INFORMATION_PATH = TIMBA_DATA_DIR / "input/02_Additional_Information/additional_information.xlsx"
WORLDPRICE_PATH = TIMBA_DATA_DIR / "input/02_Additional_Information/worldprice_world500.xlsx"
PKL_WORLD_PATH = TIMBA_DATA_DIR / "input/03_Serialization/WorldDataContent.pkl"
PKL_ADD_INFO_PATH = TIMBA_DATA_DIR / "input/03_Serialization/AddInfoContent.pkl"
PKL_WORLDPRICE_PATH = TIMBA_DATA_DIR / "input/03_Serialization/WorldPriceContent.pkl"

# output
RESULTS_OUTPUT = TIMBA_DATA_DIR / "output/results_D"
RESULTS_OUTPUT_AGG = TIMBA_DATA_DIR / "output/results_aggregated_D"
FOREST_OUTPUT = TIMBA_DATA_DIR / "output/forest_D"
WORLD_PRICE_OUTPUT = TIMBA_DATA_DIR / "output/world_prices_D"
MANUFACTURE_OUTPUT = TIMBA_DATA_DIR / "output/manufacture_D"
LOGGING_OUTPUT_FOLDER = TIMBA_DATA_DIR / "output"
PKL_OUTPUT_PATH = TIMBA_DATA_DIR / "output/pkl"

# plot
OUTPUT_FILE = "\\data\\output\\results_D*.csv"
OUTPUT_DIR = "\\data\\output\\"
INPUT_DIR = "\\analysis\\Data\\TiMBA\\"
