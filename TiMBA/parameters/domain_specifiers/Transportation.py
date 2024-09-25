from TiMBA.parameters.domain_specifiers.AbstractDomainSpecifier import DomainNameSpecifier, SplitDomainSpecifier, \
    MainDomainSpecifier, SubDomainSpecifier, FinalDomainSpecifier, RegionCodeSpecifier


class TransportationImport(DomainNameSpecifier, RegionCodeSpecifier, FinalDomainSpecifier, SubDomainSpecifier):
    origin_region = "originCountry"
    Import = "Import"

    region_code = "destinationCountry"
    commodity_code = "CommodityCode"
    freight_cost = "FreightCost"
    import_ad_valorem_tax_rate = "ImportTax"
    export_ad_valorem_tax_rate = "ExportTax"
    quantity = "Transport"
    elasticity_trade_exporter = "GDPElastTransExp"
    elasticity_trade_importer = "GDPElastTransImp"
    trade_inertia_bounds = "TradeInertias"
    price = "PriceCountryorigin"
    elasticity_price = "TElast"

    # Column Mapper
    header_description = {
        "****** TRANSPORTATION COST AND TAX ******": origin_region,
        "Unnamed: 2": region_code,
        "Unnamed: 4": commodity_code,
        "Unnamed: 5": freight_cost,
        "Unnamed: 6": import_ad_valorem_tax_rate,
        "Unnamed: 7": export_ad_valorem_tax_rate,
        "Unnamed: 8": quantity,
        "Unnamed: 9": elasticity_trade_exporter,
        "Unnamed: 10": elasticity_trade_importer,
        "Unnamed: 11": trade_inertia_bounds,
        "Unnamed: 12": price,
        "Unnamed: 13": elasticity_price
    }

    # Excel Start Idx
    splitting_mask = "zz"
    column_index = 0
    mask_axis = 0


class TransportationExport(DomainNameSpecifier, RegionCodeSpecifier, FinalDomainSpecifier, SubDomainSpecifier):
    region_code = "originRegion"
    Export = "Export"

    destination_region = "destinationCountry"
    commodity_code = "CommodityCode"
    freight_cost = "FreightCost"
    import_ad_valorem_tax_rate = "ImportTax"
    export_ad_valorem_tax_rate = "ExportTax"
    quantity = "Transport"
    elasticity_trade_exporter = "GDPElastTransExp"
    elasticity_trade_importer = "GDPElastTransImp"
    trade_inertia_bounds = "TradeInertias"
    price = "PriceCountryorigin"
    elasticity_price = "TElast"

    # Column Mapper
    header_description = {
        "****** TRANSPORTATION COST AND TAX ******": region_code,
        "Unnamed: 2": destination_region,
        "Unnamed: 4": commodity_code,
        "Unnamed: 5": freight_cost,
        "Unnamed: 6": import_ad_valorem_tax_rate,
        "Unnamed: 7": export_ad_valorem_tax_rate,
        "Unnamed: 8": quantity,
        "Unnamed: 9": elasticity_trade_exporter,
        "Unnamed: 10": elasticity_trade_importer,
        "Unnamed: 11": trade_inertia_bounds,
        "Unnamed: 12": price,
        "Unnamed: 13": elasticity_price
    }

    # Excel Start Idx
    splitting_mask = "zz"
    column_index = 2
    mask_axis = 0


class Transportation(DomainNameSpecifier, MainDomainSpecifier, SplitDomainSpecifier):
    # Excel Start Idx
    content_start_index = 14

    domain_split_list = [
        TransportationImport(),
        TransportationExport()
    ]
