import os.path
from os import path
from typing import Union, Tuple

from pathlib import Path

from TiMBA.results_logging.ResultsWriter import ResultsWriter
from .headers import RESULTS_HEADER, RESULTS_AGG_HEADER
from .paths import (
    INPUT_WORLD_PATH,
    ADDITIONAL_INFORMATION_PATH,
    WORLDPRICE_PATH,
    PKL_WORLD_PATH,
    PKL_ADD_INFO_PATH,
    PKL_WORLDPRICE_PATH,
    PKL_OUTPUT_PATH,
    RESULTS_OUTPUT,
    RESULTS_OUTPUT_AGG,
    FOREST_OUTPUT,
    WORLD_PRICE_OUTPUT,
    LOGGING_OUTPUT_FOLDER,
    OUTPUT_FILE,
    OUTPUT_DIR,
    INPUT_DIR
)

PKL_OUTPUT_PATH = PKL_OUTPUT_PATH
INPUT_WORLD_PATH = path.abspath(path.join(*Path(__file__).parts[:-2], INPUT_WORLD_PATH))
ADDITIONAL_INFORMATION_PATH = path.abspath(path.join(*Path(__file__).parts[:-2], ADDITIONAL_INFORMATION_PATH))
WORLDPRICE_PATH = path.abspath(path.join(*Path(__file__).parts[:-2], WORLDPRICE_PATH))
PKL_WORLD_PATH = path.abspath(path.join(*Path(__file__).parts[:-2], PKL_WORLD_PATH))
PKL_ADD_INFO_PATH = path.abspath(path.join(*Path(__file__).parts[:-2], PKL_ADD_INFO_PATH))
PKL_WORLDPRICE_PATH = path.abspath(path.join(*Path(__file__).parts[:-2], PKL_WORLDPRICE_PATH))
RESULTS_OUTPUT = path.abspath(path.join(*Path(__file__).parts[:-2], RESULTS_OUTPUT))
RESULTS_OUTPUT_AGG = path.abspath(path.join(*Path(__file__).parts[:-2], RESULTS_OUTPUT_AGG))
FOREST_OUTPUT = path.abspath(path.join(*Path(__file__).parts[:-2], FOREST_OUTPUT))
WORLD_PRICE_OUTPUT = path.abspath(path.join(*Path(__file__).parts[:-2], WORLD_PRICE_OUTPUT))
LOGGING_OUTPUT_FOLDER = path.abspath(path.join(*Path(__file__).parts[:-2], LOGGING_OUTPUT_FOLDER))


def get_results_writer(output_path: Union[str, Path, None], agg_flag: bool) -> ResultsWriter:
    """
    Spawns instance of Resultswriter based on user input. Allows to differentiate between exhaustive and aggregated
    results.
    :param output_path: Folderpath given by user
    :return: Instance of ResultsWriter
    """
    if agg_flag is not True:
        if output_path is None:
            return ResultsWriter(RESULTS_OUTPUT, filetype=".csv", overwrite_file=False, header=RESULTS_HEADER)
        else:
            fp = os.path.join(output_path, r"output/results.csv")
            if not os.path.exists(output_path):
                os.makedirs(fp, exist_ok=True)
            return ResultsWriter(fp, filetype=".csv", overwrite_file=False, header=RESULTS_HEADER)
    else:
        if output_path is None:
            return ResultsWriter(RESULTS_OUTPUT_AGG, filetype=".csv", overwrite_file=False, header=RESULTS_AGG_HEADER)
        else:
            fp = os.path.join(output_path, r"output/results_aggregated.csv")
            if not os.path.exists(output_path):
                os.makedirs(fp, exist_ok=True)
            return ResultsWriter(fp, filetype=".csv", overwrite_file=False, header=RESULTS_AGG_HEADER)


def get_pkl_paths(output_path: Union[str, Path, None]) -> Tuple[str, str, str]:
    """
    Returns correct paths for and of serialized pkl-files based on user input.
    :param output_path: Folderpath given by user
    :return: tuple of strings being paths
    """
    if output_path is None:
        return PKL_WORLD_PATH, PKL_ADD_INFO_PATH, PKL_WORLDPRICE_PATH
    else:
        pkl_world_path = os.path.join(output_path, *Path(PKL_WORLD_PATH).parts[-2:])
        pkl_add_info_path = os.path.join(output_path, *Path(PKL_ADD_INFO_PATH).parts[-2:])
        pkl_worldprice_path = os.path.join(output_path, *Path(PKL_WORLDPRICE_PATH).parts[-2:])
        return pkl_world_path, pkl_add_info_path, pkl_worldprice_path


def get_global_paths(output_path: Union[str, Path, None], worldversion: str) -> Tuple[str, str, str]:
    """
    Returns correct paths for files based on user input.
    :param output_path: Folderpath given by user
    :return: tuple of strings being paths
    """
    if output_path is None:
        if worldversion is None:
            return INPUT_WORLD_PATH, ADDITIONAL_INFORMATION_PATH, WORLDPRICE_PATH
        else:
            input_world_path = INPUT_WORLD_PATH + "/" + worldversion
            input_world_path = path.abspath(path.join(*Path(__file__).parts[:-2], input_world_path))
            # os.makedirs(input_world_path, exist_ok=True)
            return input_world_path, ADDITIONAL_INFORMATION_PATH, WORLDPRICE_PATH
    else:
        input_world_path = os.path.join(output_path, *Path(INPUT_WORLD_PATH).parts[-2:])
        additional_information_path = os.path.join(output_path, *Path(ADDITIONAL_INFORMATION_PATH).parts[-2:])
        worldprice_path = os.path.join(output_path, *Path(WORLDPRICE_PATH).parts[-2:])
        return input_world_path, additional_information_path, worldprice_path


def get_output_paths(package_dir, time_stamp: str, sc_name: str, PKL_OUTPUT_PATH=PKL_OUTPUT_PATH):
    """
    Collect outpaths for pkl files.
    :param package_dir: absolute folder of the model on any environment.
    :param time_stamp: time stamp from main
    :param sc_name: scenario name from main
    :param PKL_OUTPUT_PATH: path to pkl output
    :return: output paths for the pkl files
    """
    import glob
    OUTPUT_PATH = str(package_dir) + OUTPUT_DIR
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    file_name = "DataContainer_Sc_" + sc_name
    try:
        latest_file = max(list())
        used_sc_names = [s for s in os.listdir(OUTPUT_PATH) if sc_name in s]
        OUTPUT_PATH = OUTPUT_PATH + file_name + f"_{time_stamp}" + str(len(used_sc_names)) + ".pkl"
        PKL_OUTPUT_PATH = PKL_OUTPUT_PATH + file_name + f"_{time_stamp}" + str(len(used_sc_names)) + ".pkl"
    except ValueError:
        OUTPUT_PATH = OUTPUT_PATH + file_name + ".pkl"
        PKL_OUTPUT_PATH = PKL_OUTPUT_PATH + file_name + f"_{time_stamp}" + ".pkl"
        latest_file = str(package_dir) + OUTPUT_DIR + f"results_D{time_stamp}" + "_" + sc_name + ".xlsx" + ".csv"

    return OUTPUT_PATH, latest_file, PKL_OUTPUT_PATH


__all__ = [
    "get_results_writer",
    "get_global_paths",
    "INPUT_WORLD_PATH",
    "ADDITIONAL_INFORMATION_PATH",
    "WORLDPRICE_PATH",
    "RESULTS_OUTPUT",
    "LOGGING_OUTPUT_FOLDER"
]
