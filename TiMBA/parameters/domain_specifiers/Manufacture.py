from TiMBA.parameters.domain_specifiers.AbstractDomainSpecifier import DomainNameSpecifier, SplitDomainSpecifier, \
    MainDomainSpecifier, SubDomainSpecifier, FinalDomainSpecifier, RegionCodeSpecifier


class ManufactureCost(DomainNameSpecifier, RegionCodeSpecifier, FinalDomainSpecifier, SubDomainSpecifier):
    region_code = "RegionCode"
    manufacture_cost = "Item"

    process_number = "Process_number"
    commodity_code = "CommodityCode"
    input_mix_number = "Input_mix_number"
    net_manufacturing_cost = "ManuCost"
    quantity = "Manufacture"
    elasticity_price = "MElast"

    # Column Mapper
    header_description = {
        "****** MANUFACTURE ******": manufacture_cost,
        "Unnamed: 1": region_code,
        "Unnamed: 3": commodity_code,
        "Unnamed: 5": process_number,
        "Unnamed: 6": input_mix_number,
        "Unnamed: 7": net_manufacturing_cost,
        "Unnamed: 8": quantity,
        "Unnamed: 9": elasticity_price,
    }

    # Excel Start Idx
    splitting_mask = "M"
    column_index = 0
    mask_axis = 0


class ManufactureCoefficients(DomainNameSpecifier, RegionCodeSpecifier, FinalDomainSpecifier, SubDomainSpecifier):
    region_code = "RegionCode"
    manufacture_coefficient = "Item"

    commodity_code = "InputCommodity"
    output_commodity = "OutputCommodity"
    process_number = "Process_number"
    input_mix_number = "Input_mix_number"
    quantity = "ManuFakt"
    elasticity_price = "Output_elasticity_of_manufacturing_costs"
    input_commodity_per_unit_output_commodity = "Amount_of_input_commodity_per_unit_of_output_commodity"

    header_description = {
        "****** MANUFACTURE ******": manufacture_coefficient,
        "Unnamed: 1": region_code,
        "Unnamed: 3": commodity_code,
        "Unnamed: 4": output_commodity,
        "Unnamed: 5": process_number,
        "Unnamed: 6": input_mix_number,
        "Unnamed: 7": quantity,
        "Unnamed: 8": elasticity_price,
        "Unnamed: 9": input_commodity_per_unit_output_commodity,
    }

    # Excel Start Idx
    splitting_mask = "P"
    column_index = 0
    mask_axis = 0

    # Default IO-coefficients
    default_IO = {
        80: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        81: [0, 0, 0, 3, 3, 1.5, 1.5, 4, 4, 0, 0, 0, 0, 0],
        82: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        83: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        84: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        85: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        86: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        87: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.1, 1.1, 1.1],
        88: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.1, 1.1, 1.1],
        89: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.1, 1.1, 1.1],
        90: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.1, 1.1, 1.1],
        91: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        92: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        93: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    }


class Manufacture(DomainNameSpecifier, MainDomainSpecifier, SplitDomainSpecifier):
    # Excel Start Idx
    content_start_index = 29

    domain_split_list = [
        ManufactureCost(),
        ManufactureCoefficients()
    ]
