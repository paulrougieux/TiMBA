from pathlib import Path
import os
import unittest
from sys import argv
import pandas as pd
import numpy as np

from TiMBA.parameters.headers import RESULTS_HEADER
from TiMBA.parameters import INPUT_WORLD_PATH, WORLDPRICE_PATH, ADDITIONAL_INFORMATION_PATH
from TiMBA.results_logging.base_logger import get_logger
from TiMBA.results_logging.ResultsWriter import ResultsWriter
from TiMBA.data_management.DataManager import DataManager
from TiMBA.data_management.DataContainer import DataContainer, WorldDataCollector, AdditionalInformation
from TiMBA.logic.model import TiMBA
from TiMBA.user_io.default_parameters import user_input
from TiMBA.data_management.ParameterCollector import ParameterCollector
from TiMBA.parameters.Defines import SolverParameters
from TiMBA.data_validation.DataValidator import DataValidator

INPUT_UNIT_TEST_TIMBA_RESULT = (os.path.abspath(os.path.join(*Path(__file__).parts[:-1],
                                                             r"test_data/DataContainer_Sc_scenario_input.pkl")))


TEMPORARY_RESULT_FILE = os.path.abspath(os.path.join(*Path(__file__).parts[:-1], r".pytest_cache/tmp.csv"))
TEMPORARY_TESTLOG_FILE = os.path.abspath(os.path.join(*Path(__file__).parts[:-1], r".pytest_cache"))

world_version_unit_test = os.listdir(INPUT_WORLD_PATH)[0]

os.environ["MAX_PERIOD"] = "1"

class TestTiMBAClass(unittest.TestCase):
    data_timba_test = DataManager.restore_from_pickle(INPUT_UNIT_TEST_TIMBA_RESULT)

    WorldDataCont = WorldDataCollector(INPUT_WORLD_PATH + "/" + world_version_unit_test)
    AddInfoCont = AdditionalInformation(ADDITIONAL_INFORMATION_PATH)
    WorldPriceCont = DataContainer(WORLDPRICE_PATH)
    Logger = get_logger(TEMPORARY_TESTLOG_FILE)
    ResultsHandler = ResultsWriter(TEMPORARY_RESULT_FILE, overwrite_file=True, header=RESULTS_HEADER)
    UserData = ParameterCollector(user_input=user_input)

    flag_test_result_activate = user_input["test_timba_results"]
    def setUp(self):
        self.max_period = os.environ["MAX_PERIOD"]
    def test_timba_run(self, test_activate=flag_test_result_activate, DataTest=data_timba_test):

        try:
            self.UserData.max_period = int(os.environ["MAX_PERIOD"])
            print(f"Test suite is running with a user-defined number of {self.UserData.max_period} periods ")
            print(DataTest.keys())
        except KeyError:
            print(f"Test suite is running with a default number of {self.UserData.max_period} periods")

        DataManager.readin_preprocess(WorldData=self.WorldDataCont,
                                      AdditionalInfo=self.AddInfoCont,
                                      WorldPrices=self.WorldPriceCont,
                                      UserOptions=self.UserData,
                                      Logger=self.Logger)

        data_ooptimba = TiMBA(Data=self.WorldDataCont,
                              UserOptions=self.UserData,
                              AdditionalInfo=self.AddInfoCont,
                              WorldPriceData=self.WorldPriceCont,
                              LogHandler=self.Logger,
                              ResultHandler=self.ResultsHandler)

        data_ooptimba.compute(max_iteration=SolverParameters.MAX_ITERATION_UNIT_TEST.value,
                              rel_accuracy=SolverParameters.REL_ACCURACY_UNIT_TEST.value,
                              abs_accuracy=SolverParameters.ABS_ACCURACY_UNIT_TEST.value,
                              dynamization_activated=True,
                              constants=[False, False, False],
                              capped_prices=False)

        if test_activate:
            self.assertTrue(
                DataValidator.check_timba_results(Data=self.WorldDataCont, DataTest=DataTest, rel_tolerance=10e-02),
                "Produced TiMBA results do not correspond to provided validation results")


if __name__ == '__main__':
    unittest.main()
