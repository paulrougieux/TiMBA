from TiMBA.parameters.Domains import Domains
from TiMBA.parameters.domain_specifiers.AbstractDomainSpecifier import *

# IMPORTANT: This list must be in correct order wrt to domains to be split.
__full_set__ = [
    Domains.Specification,
    Domains.Regions,
    Domains.Commodities,
    Domains.Supply,
    Domains.RecyclingS,
    Domains.Forest,
    Domains.Demand,
    Domains.Manufacture,
    Domains.ManufactureCost,
    Domains.ManufactureCoefficients,
    Domains.Transportation,
    Domains.TransportationImport,
    Domains.TransportationExport,
    Domains.ExogChange,
    Domains.ExogChangeTrade,
    Domains.ExogChangeSupply,
    Domains.ExogChangeDemand,
    Domains.ExogChangeForest,
    Domains.ExogChangeManufactureCost,
    Domains.ExogChangeManufactureCoefficients,
    Domains.ExogChangeTradeImport,
    Domains.ExogChangeTradeExport
]

main_domains_list = list(filter(lambda domain: issubclass(domain.__class__, MainDomainSpecifier), __full_set__))
final_domains_list = list(filter(lambda domain: issubclass(domain.__class__, FinalDomainSpecifier), __full_set__))
domains_to_split_list = list(filter(lambda domain: issubclass(domain.__class__, SplitDomainSpecifier), __full_set__))
drop_description_domains_list = main_domains_list[1:].copy()

domains_to_align_list = [
    Domains.Demand,
    Domains.Supply,
    Domains.TransportationExport,
    Domains.TransportationImport,
    Domains.ManufactureCost,
    Domains.ManufactureCoefficients,
    Domains.ExogChangeDemand,
    Domains.ExogChangeSupply,
    Domains.ExogChangeTradeExport,
    Domains.ExogChangeTradeImport,
    Domains.ExogChangeManufactureCost,
    Domains.ExogChangeManufactureCoefficients
]

domains_to_optimize_list = [
    Domains.Demand,
    Domains.TransportationExport,
    Domains.TransportationImport,
    Domains.ManufactureCost,
    Domains.Supply
]

domains_to_update_list = [
    Domains.Demand,
    Domains.TransportationExport,
    Domains.TransportationImport,
    Domains.ManufactureCost,
    Domains.Supply,
    Domains.ManufactureCoefficients,
    Domains.Forest
]
