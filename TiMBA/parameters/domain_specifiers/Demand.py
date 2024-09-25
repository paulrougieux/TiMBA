from TiMBA.parameters.domain_specifiers.AbstractDomainSpecifier import DomainNameSpecifier, MainDomainSpecifier, \
    FinalDomainSpecifier


class Demand(DomainNameSpecifier, MainDomainSpecifier, FinalDomainSpecifier):
    # Read-In columns
    region_code = "RegionCode"
    commodity_code = "CommodityCode"

    # Column names
    price = "DPrice"
    quantity = "Demand"
    elasticity_price = "DElast"
    elasticity_gdp = "DGDPElast0"
    elasticity_expectations = "DExpectations"
    lower_bound = "DLB"
    upper_bound = "DUB"

    # Column Mapper
    header_description = {
        "****** DEMAND ******": region_code,
        "Unnamed: 1": commodity_code,
        "Unnamed: 2": price,
        "Unnamed: 3": quantity,
        "Unnamed: 4": elasticity_price,
        "Unnamed: 5": elasticity_gdp,
        "Unnamed: 6": elasticity_expectations,
        "Unnamed: 12": lower_bound,
        "Unnamed: 13": upper_bound
    }

    # Excel Start Idx
    content_start_index = 17
