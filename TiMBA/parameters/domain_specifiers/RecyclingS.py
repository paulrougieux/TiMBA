from TiMBA.parameters.domain_specifiers.AbstractDomainSpecifier import DomainNameSpecifier, MainDomainSpecifier, \
    FinalDomainSpecifier


class RecyclingS(DomainNameSpecifier, MainDomainSpecifier, FinalDomainSpecifier):
    # Read-In columns
    region_code = "RegionCode"
    commodity_code = "CommodityCode"

    # Column names
    recov_commodity = "recovCommodity"
    used_commodity = "usedCommodity"
    fraction_consumption = "fraction_consumption"
    recov_lbs = "recovlbs"
    recov_ubs = "recovubs"

    # Column Mapper
    header_description = {
        "****** RECYCLING (SUPPLY) ******": region_code,
        "Unnamed: 2": recov_commodity,
        "Unnamed: 4": used_commodity,
        "Unnamed: 5": fraction_consumption,
        "Unnamed: 6": recov_lbs,
        "Unnamed: 7": recov_ubs
    }

    # Excel Start Idx
    content_start_index = 8
