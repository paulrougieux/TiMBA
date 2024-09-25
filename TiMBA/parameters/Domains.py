from TiMBA.parameters.domain_specifiers.Specification import Specification, Regions, Commodities
from TiMBA.parameters.domain_specifiers.Demand import Demand
from TiMBA.parameters.domain_specifiers.Forest import Forest
from TiMBA.parameters.domain_specifiers.Supply import Supply
from TiMBA.parameters.domain_specifiers.RecyclingS import RecyclingS
from TiMBA.parameters.domain_specifiers.Manufacture import Manufacture, ManufactureCost, ManufactureCoefficients
from TiMBA.parameters.domain_specifiers.Transportation import Transportation, TransportationImport, TransportationExport
from TiMBA.parameters.domain_specifiers.ExogChange import (
    ExogChange, ExogChangeSupply, ExogChangeDemand, ExogChangeForest, ExogChangeTrade, ExogChangeManufactureCost,
    ExogChangeManufactureCoefficients, ExogChangeTradeImport, ExogChangeTradeExport)


class Domains:
    """
    We define a dictionary for string access specifiers to have maintainable access on Excel sheet.
    """
    Demand = Demand()
    Forest = Forest()
    Supply = Supply()
    RecyclingS = RecyclingS()

    Specification = Specification()
    Regions = Regions()
    Commodities = Commodities()

    Manufacture = Manufacture()
    ManufactureCost = ManufactureCost()
    ManufactureCoefficients = ManufactureCoefficients()

    Transportation = Transportation()
    TransportationImport = TransportationImport()
    TransportationExport = TransportationExport()

    ExogChange = ExogChange()
    ExogChangeSupply = ExogChangeSupply()
    ExogChangeDemand = ExogChangeDemand()
    ExogChangeForest = ExogChangeForest()
    ExogChangeTrade = ExogChangeTrade()
    ExogChangeTradeImport = ExogChangeTradeImport()
    ExogChangeTradeExport = ExogChangeTradeExport()
    ExogChangeManufactureCoefficients = ExogChangeManufactureCoefficients()
    ExogChangeManufactureCost = ExogChangeManufactureCost()


RestOfWorld = {
    Regions.region_code: ["zy"],
    Regions.region_name: ["Rest of World"]
}
