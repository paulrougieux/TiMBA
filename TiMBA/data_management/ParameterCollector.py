from pathlib import Path

from typing import Union


class ParameterCollector:
    """
    Class to collect user IO and propagate through application.
    """
    def __init__(self, user_input: dict, folderpath: Union[str, Path, None] = None):
        """
        :param year: ...
        :param max_period: ...
        :param country: ...
        :param product: ...
        :param calc_product_prices: Switch to enable/disable shadow-price calc
        :param transportation_imp_exp_bound_factor: Factor to be used in model.set_bounds() for import/export
        :param param_x: EXEMPLARY ADDITIONAL PARAM  TODO: Drop
        :param param_y: EXEMPLARY ADDITIONAL PARAM  TODO: Drop
        """
        self._year = user_input['year']
        self._max_period = user_input['max_period']
        self._calc_product_prices = user_input['product_price']
        self._calc_world_prices = user_input['world_price']
        self._transportation_imp_exp_bound_factor = user_input['transportation_factor']
        self._material_balance = user_input['material_balance']
        self._global_material_balance = user_input['global_material_balance']
        self._serialization = user_input['serialization']
        self._constants = user_input['constants']
        self._dynamization_activated = user_input['dynamization_activated']
        self._capped_prices = user_input['capped_prices']
        self._cleaned_opt_quantity = user_input['cleaned_opt_quantity']
        self._verbose_optimization_logger = user_input['verbose_optimization_logger']
        self._verbose_calculation_logger = user_input['verbose_calculation_logger']
        self._addInfo = user_input['addInfo']
        self._folderpath = folderpath

        # Run directly after __init__ to ensure correct user IO
        self.input_data_check()

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int):
        self._year = value

    @property
    def max_period(self) -> int:
        return self._max_period

    @max_period.setter
    def max_period(self, value: int):
        self._max_period = value

    @property
    def calc_product_prices(self) -> str:
        return self._calc_product_prices

    @calc_product_prices.setter
    def calc_product_prices(self, value: str):
        self._calc_product_prices = value

    @property
    def calc_world_prices(self) -> str:
        return self._calc_world_prices

    @calc_world_prices.setter
    def calc_world_prices(self, value: str):
        self._calc_world_prices = value

    @property
    def transportation_imp_exp_bound_factor(self) -> float:
        return self._transportation_imp_exp_bound_factor

    @transportation_imp_exp_bound_factor.setter
    def transportation_imp_exp_bound_factor(self, value: float):
        self._transportation_imp_exp_bound_factor = value

    @property
    def material_balance(self) -> str:
        return self._material_balance

    @material_balance.setter
    def material_balance(self, value: str):
        self._material_balance = value

    @property
    def global_material_balance(self) -> str:
        return self._global_material_balance

    @global_material_balance.setter
    def global_material_balance(self, value: str):
        self._global_material_balance = value

    @property
    def serialization(self) -> bool:
        return self._serialization

    @serialization.setter
    def serialization(self, value: bool):
        self._serialization = value

    @property
    def constants(self) -> list:
        return self._constants

    @constants.setter
    def constants(self, value: str):
        self._constants = value

    @property
    def dynamization_activated(self) -> bool:
        return self._dynamization_activated

    @dynamization_activated.setter
    def dynamization_activated(self, value: bool):
        self._dynamization_activated = value

    @property
    def capped_prices(self) -> bool:
        return self._capped_prices

    @capped_prices.setter
    def capped_prices(self, value: bool):
        self._capped_prices = value

    @property
    def verbose_optimization_logger(self) -> bool:
        return self._verbose_optimization_logger

    @verbose_optimization_logger.setter
    def verbose_optimization_logger(self, value: bool):
        self._verbose_optimization_logger = value

    @property
    def verbose_calculation_logger(self) -> bool:
        return self._verbose_calculation_logger

    @verbose_calculation_logger.setter
    def verbose_calculation_logger(self, value: bool):
        self._verbose_calculation_logger = value

    @property
    def addInfo(self) -> bool:
        return self._addInfo

    @addInfo.setter
    def addInfo(self, value: bool):
        self._addInfo = value

    @property
    def folderpath(self) -> Union[str, Path, None]:
        return self._folderpath

    @folderpath.setter
    def folderpath(self, value: Union[str, Path, None]):
        self._folderpath = value

    @property
    def cleaned_opt_quantity(self) -> bool:
        return self._cleaned_opt_quantity

    @cleaned_opt_quantity.setter
    def cleaned_opt_quantity(self, value: bool):
        self._cleaned_opt_quantity = value

    def __repr__(self):
        return repr(f"year={self.year}, "
                    f"max_period={self.max_period}, "
                    f"calc_product_prices={self.calc_product_prices}, "
                    f"calc_world_prices={self.calc_world_prices}, "
                    f"transportation_imp_exp_bound_factor={self.transportation_imp_exp_bound_factor}"
                    f"material_balance={self.material_balance}, "
                    )

    def input_data_check(self):
        assert isinstance(self.year, int)
        assert isinstance(self.max_period, int)
        assert isinstance(self.calc_product_prices, str)
        assert isinstance(self.calc_world_prices, str)
        assert isinstance(self.material_balance, str)
        assert isinstance(self.global_material_balance, bool)
        assert isinstance(self.serialization, bool)
        assert isinstance(self.constants, list)
        assert isinstance(self.dynamization_activated, bool)
        assert isinstance(self.capped_prices, bool)
        assert isinstance(self.cleaned_opt_quantity, bool)
        assert isinstance(self.verbose_optimization_logger, bool)
        assert isinstance(self.verbose_calculation_logger, bool)
        assert isinstance(self.addInfo, bool)
        assert type(self.transportation_imp_exp_bound_factor) in [float, int]

        # TODO: Adapt tests for new params: Following are just exemplary.
        # assert self.param_x[0] > 0
        # assert isinstance(self.param_x[0], int)
        # assert -1 < self.param_x[1] < 1
        # assert len(self.param_y) == 3
        # assert isinstance(self.param_y[0], str)
        # assert isinstance(self.param_y[1], int)
        # assert isinstance(self.param_y[2], float)
        # assert self.param_y[2] > 2
