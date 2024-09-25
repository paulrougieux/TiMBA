from TiMBA.parameters.domain_specifiers.AbstractDomainSpecifier import DomainNameSpecifier, MainDomainSpecifier, \
    FinalDomainSpecifier


class Forest(DomainNameSpecifier, MainDomainSpecifier, FinalDomainSpecifier):
    region_code = "RegionCode"

    gdp_per_capita_base_period = "FGDPCap"
    forest_stock = "ForStock"
    growth_rate_forest_stock = "ForStockGrowth"
    elasticity_growth_rate_forest_stock = "StockElastArea"
    forest_area = "ForArea"
    forest_area_growth_rate = "ForAreaGrowth"
    linear_gdp_forest_area_growth_rate = "ForAreaGDPGrowth"
    exponential_gdp_forest_area_growth_rate = "SqForAreaGDPGrowth"
    fraction_fuelwood = "FuelwoodForest"
    ratio_inventory_drain = "InventoryDrain"
    max_ratio_inventory_drain = "MaxRatioInventoryDrain"
    CO2_growing_stock = "WoodCO2"
    price_CO2 = "CO2Price"
    alpha =  "alpha"
    gamma = "gamma"
    periodic_growth_rate_of_forest_area = "ga"
    forest_growth_without_harvest = "gu"
    supply_from_forest = "supply_from_forest"

    # Column Mapper
    header_description = {
            "****** FOREST RESOURCE ******": region_code,
            "Unnamed: 1": gdp_per_capita_base_period,
            "Unnamed: 2": forest_stock,
            "Unnamed: 3": growth_rate_forest_stock,
            "Unnamed: 4": elasticity_growth_rate_forest_stock,
            "Unnamed: 5": forest_area,
            "Unnamed: 6": forest_area_growth_rate,
            "Unnamed: 7": linear_gdp_forest_area_growth_rate,
            "Unnamed: 8": exponential_gdp_forest_area_growth_rate,
            "Unnamed: 9": fraction_fuelwood,
            "Unnamed: 10": ratio_inventory_drain,
            "Unnamed: 11": max_ratio_inventory_drain,
            "Unnamed: 12": CO2_growing_stock,
            "Unnamed: 13": price_CO2
    }

    # Excel Start Idx
    content_start_index = 16
