from TiMBA.parameters.domain_specifiers.AbstractDomainSpecifier import (
    DomainNameSpecifier, RegionCodeSpecifier, FinalDomainSpecifier, SubDomainSpecifier, CommodityCodeSpecifier,
    SplitDomainSpecifier, MainDomainSpecifier)


class Regions(DomainNameSpecifier, RegionCodeSpecifier, FinalDomainSpecifier, SubDomainSpecifier):
    region_code = "RegionCode"
    region_name = "RegionName"

    # Column Mapper
    header_description = {
        "Region Code": region_code,
        "Region Name": region_name
    }

    splitting_mask = ["Region Code", "Region Name"]
    column_index = None
    mask_axis = 1


class Commodities(DomainNameSpecifier, CommodityCodeSpecifier, FinalDomainSpecifier, SubDomainSpecifier):
    commodity_code = "CommodityCode"
    commodity_name = "CommodityName"

    # Column Mapper
    header_description = {
        "Commodity Name": commodity_name,
        "Commodity Code": commodity_code
    }

    splitting_mask = ["Commodity Code", "Commodity Name"]
    column_index = None
    mask_axis = 1


class Specification(DomainNameSpecifier, MainDomainSpecifier, SplitDomainSpecifier):
    # Excel Start Idx
    content_start_index = 0

    domain_split_list = [
        Regions(),
        Commodities()
    ]
