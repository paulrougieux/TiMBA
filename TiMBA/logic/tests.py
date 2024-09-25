import pandas as pd
import numpy as np
from TiMBA.parameters.Defines import (Constants, Shifter, ConversionParameters, VarNames)

from TiMBA.helpers.utils import Domains
from TiMBA.data_management.DataContainer import InterfaceWorldData


def verify_trade_balance(world_data: InterfaceWorldData, user_option, logger: classmethod,
                         verification_threshold: int):
    """
    Verifies if optimized trade quantities comply with the global trade constraint (sum exports == sum imports)
    :params world_data: interface world data
    :params user_option: parameter collector of user settings
    :params logger: model logger
    :params verification_threshold: threshold of allowed deviations from the verified constaint
    """
    export_sum = world_data.TransportationExport.data_aligned[
        [Domains.TransportationExport.commodity_code, Domains.TransportationExport.quantity]]
    export_sum = export_sum.groupby(Domains.TransportationExport.commodity_code).sum()
    import_sum = world_data.TransportationImport.data_aligned[
        [Domains.TransportationImport.commodity_code, Domains.TransportationImport.quantity]]
    import_sum = import_sum.groupby(Domains.TransportationImport.commodity_code).sum()
    verification = export_sum - import_sum
    unbalanced_commodities = verification[
        (verification[Domains.TransportationExport.quantity] >= verification_threshold) |
        (verification[Domains.TransportationExport.quantity] <= -verification_threshold)]

    if user_option.verbose_calculation_logger:
        logger.info(f"Verification Trade Balance (sum_import == sum_export)")
    if not unbalanced_commodities.any().any():
        logger.info(f"Trade balance for all commodities is satisfied")
    else:
        logger.info(f"Trade balance for following commodities is not satisfied")
        if user_option.verbose_calculation_logger:
            logger.info(f"{unbalanced_commodities}")


def verify_material_balance(world_data: InterfaceWorldData, user_option, logger: classmethod,
                            verification_threshold: int):
    """
    Verifies if optimized quantities comply with the material balance for each country and commodity
    :params world_data: interface world data
    :params user_option: parameter collector of user settings
    :params logger: model logger
    :params verification_threshold: threshold of allowed deviations from the verified constaint
    """
    index_verification = len(world_data.data_aligned) - len(world_data.Commodities.data)
    material_balance = (world_data.Demand.data_aligned[Domains.Demand.quantity] +
                        world_data.TransportationExport.data_aligned[Domains.TransportationExport.quantity] +
                        pd.DataFrame(world_data.ManufactureCoefficients.ioMatrix.dot(np.array(
                            world_data.ManufactureCost.data_aligned[Domains.ManufactureCost.quantity])))[0] -
                        world_data.Supply.data_aligned[Domains.Supply.quantity] -
                        world_data.TransportationImport.data_aligned[Domains.TransportationImport.quantity] -
                        world_data.ManufactureCost.data_aligned[Domains.ManufactureCost.quantity]
                        ).iloc[:index_verification]

    material_balance = pd.concat([
        world_data.data_aligned, material_balance], axis=1)[[Domains.Regions.region_code,
                                                             Domains.Commodities.commodity_code, 0]]

    if user_option.verbose_calculation_logger:
        logger.info(f"Verification Material Balance:")
    unbalanced_region = material_balance[(material_balance[0] >= verification_threshold) |
                                         (material_balance[0] <= -verification_threshold)]

    if not unbalanced_region.any().all():
        logger.info(f"Material Balance for all regions & commodities is satisfied")
    else:
        logger.info(f"Material Balance is not satisfied for {len(unbalanced_region)} regions")
        if user_option.verbose_calculation_logger:
            logger.info(f"Range of deviations. Max: {max(unbalanced_region[0])}, Min: {min(unbalanced_region[0])}")
            logger.info(f"Material Balance is not satisfied for following regions & commodities")
            logger.info(f"{unbalanced_region}")


def verify_global_material_balance(world_data: InterfaceWorldData, user_option, logger: classmethod):
    """
    Verifies if optimized quantities comply with the global material balance for each commodity
    :params world_data: interface world data
    :params user_option: parameter collector of user settings
    :params logger: model logger
    """
    global_material_balance = (
            sum(world_data.Demand.data_aligned[Domains.Demand.quantity]) +
            sum(world_data.TransportationExport.data_aligned[Domains.TransportationExport.quantity]) +
            sum(pd.DataFrame(world_data.ManufactureCoefficients.ioMatrix.dot(np.array(
                world_data.ManufactureCost.data_aligned[Domains.ManufactureCost.quantity])))[0]) -
            sum(world_data.Supply.data_aligned[Domains.Supply.quantity]) -
            sum(world_data.TransportationImport.data_aligned[Domains.TransportationImport.quantity]) -
            sum(world_data.ManufactureCost.data_aligned[Domains.ManufactureCost.quantity])
    )

    if user_option.verbose_calculation_logger:
        logger.info(f"Verification Global Material Balance:")
    if not global_material_balance == 0:
        logger.info(f"Global Material Balance is not satisfied: {global_material_balance}")
    else:
        logger.info(f"Global Material Balance for all regions & commodities is satisfied")


def verify_supply_upper_bound(world_data: InterfaceWorldData, user_option, logger: classmethod,
                              domain_col_name: str, verification_threshold: int):
    """
    Verifies if the optimized supply quantities comply with the upper bound for supply.
    :params world_data: interface world data
    :params user_option: parameter collector of user settings
    :params logger: model logger
    :params domain_col_name: column name of domains in optimization helpers
    :params verification_threshold: threshold of allowed deviations from the verified constaint
    """
    logger.info(f"Verification supply upper bound :")
    verify_supply_bound = (
            world_data.OptimizationHelpers.data[world_data.OptimizationHelpers.data[domain_col_name] == str(Domains.Supply)]
            ["upper_bound"].reset_index(drop=True) - world_data.Supply.data_aligned[Domains.Supply.quantity])
    verify_supply_bound = pd.concat([
        world_data.Supply.data_aligned[[Domains.Supply.region_code, Domains.Supply.commodity_code]],
        verify_supply_bound], axis=1)

    verify_supply_bound = verify_supply_bound[verify_supply_bound[0] < -verification_threshold]

    if not verify_supply_bound.index.any():
        logger.info(f"No supply bounds are exceeded")
    else:
        logger.info(f"Supply bounds are exceeded for {len(verify_supply_bound)} commodities")
        if user_option.verbose_calculation_logger:
            logger.info(f"Supply bounds are exceeded for following regions & commodities")
            logger.info(f"{verify_supply_bound}")


def verify_trade_bounds(world_data: InterfaceWorldData, opt_ubs: pd.Series, opt_lbs: pd.Series, user_option,
                        logger: classmethod, verification_threshold: int):
    """
    Verifies if optimized quantities comply with trade bounds.
    :params world_data: interface world data
    :params opt_ubs: Optimization upper bound
    :params opt_lbs: Optimization lower bound
    :params user_option: parameter collector of user settings
    :params logger: model logger
    :params verification_threshold: threshold of allowed deviations from the verified constaint
    """
    index = len(world_data.data_aligned)
    verification_export_ubs = (pd.DataFrame(opt_ubs[index: 2 * index]).reset_index(drop=True)[0] -
                               world_data.TransportationExport.data_aligned[Domains.TransportationExport.quantity])
    verification_export_lbs = (world_data.TransportationExport.data_aligned[Domains.TransportationExport.quantity] -
                               pd.DataFrame(opt_lbs[index: 2 * index]).reset_index(drop=True)[0])

    verification_export = pd.concat([verification_export_ubs, verification_export_lbs], axis=1)
    verification_export = verification_export[(verification_export[0] < -verification_threshold) |
                                              (verification_export[1] < -verification_threshold)]

    if not verification_export.any().all():
        logger.info(f"Export bounds are satisfied")
    else:
        logger.info(f"Export bounds are not satisfied for {len(verification_export)} commodities")
        if user_option.verbose_calculation_logger:
            logger.info(f"Export bounds are not satisfied for following regions & commodities")
            logger.info(f"{verification_export}")

    verification_import_ubs = (pd.DataFrame(opt_ubs[2 * index: 3 * index]).reset_index(drop=True)[0] -
                               world_data.TransportationImport.data_aligned[Domains.TransportationImport.quantity])
    verification_import_lbs = (world_data.TransportationImport.data_aligned[Domains.TransportationImport.quantity] -
                               pd.DataFrame(opt_lbs[2 * index: 3 * index]).reset_index(drop=True)[0])

    verification_import = pd.concat([verification_import_ubs, verification_import_lbs], axis=1)
    verification_import = verification_import[(verification_import[0] < -verification_threshold) |
                                              (verification_import[1] < -verification_threshold)]

    if not verification_import.any().all():
        logger.info(f"Import bounds are satisfied")
    else:
        logger.info(f"Import bounds are not satisfied for {len(verification_import)} commodities")
        if user_option.verbose_calculation_logger:
            logger.info(f"Import bounds are not satisfied for following regions & commodities")
            logger.info(f"{verification_import}")
