from TiMBA.parameters.domain_specifiers.AbstractDomainSpecifier import DomainNameSpecifier, MainDomainSpecifier, \
    FinalDomainSpecifier


class Supply(DomainNameSpecifier, MainDomainSpecifier, FinalDomainSpecifier):
    region_code = "RegionCode"
    commodity_code = "CommodityCode"

    price = "SPrice"
    quantity = "Supply"
    elasticity_price = "SElast"
    elasticity_gdp = "SGDPElast"
    elasticity_stock = "StockElast"
    elasticity_area = "AreaElast"
    elasticity_fourth = "elasticity_fourth"
    elasticity_fifth = "elasticity_fifth"
    elasticity_sixth = "elasticity_sixth"
    elasticity_respect_previous_period_supply = "elasticity_respect_previous_period_supply"
    lower_bound = "SLB"
    upper_bound = "SUB"
    last_period_quantity = "last_period_quantity"

    # Column Mapper
    header_description = {
        "****** SUPPLY ******": region_code,
        "Unnamed: 1": commodity_code,
        "Unnamed: 2": price,
        "Unnamed: 3": quantity,
        "Unnamed: 4": elasticity_price,
        "Unnamed: 5": elasticity_gdp,
        "Unnamed: 6": elasticity_stock,
        "Unnamed: 7": elasticity_area,
        "Unnamed: 8": elasticity_fourth,
        "Unnamed: 9": elasticity_fifth,
        "Unnamed: 10": elasticity_sixth,
        "Unnamed: 11": elasticity_respect_previous_period_supply,
        "Unnamed: 12": lower_bound,
        "Unnamed: 13": upper_bound,
        "Unnamed: 14": last_period_quantity,
    }

    # Excel Start Idx
    content_start_index = 17
