import unittest

from TiMBA.parameters.domain_lists import main_domains_list, final_domains_list, domains_to_split_list
from TiMBA.parameters.Domains import Domains


class TestDomainLists(unittest.TestCase):
    correct_main_domains_list = [
        Domains.Specification,
        Domains.Supply,
        Domains.RecyclingS,
        Domains.Forest,
        Domains.Demand,
        Domains.Manufacture,
        Domains.Transportation,
        Domains.ExogChange
    ]
    correct_final_domain_list = [
        Domains.Regions,
        Domains.Commodities,
        Domains.Demand,
        Domains.Forest,
        Domains.Supply,
        Domains.RecyclingS,
        Domains.ManufactureCost,
        Domains.ManufactureCoefficients,
        Domains.TransportationImport,
        Domains.TransportationExport,
        Domains.ExogChangeSupply,
        Domains.ExogChangeDemand,
        Domains.ExogChangeForest,
        Domains.ExogChangeManufactureCost,
        Domains.ExogChangeManufactureCoefficients,
        Domains.ExogChangeTradeImport,
        Domains.ExogChangeTradeExport
    ]
    correct_domains_to_split_list = [
        Domains.Specification,
        Domains.Manufacture,
        Domains.ExogChange,
        Domains.ExogChangeTrade,
        Domains.Transportation
    ]

    def test_main_domains_lists(self):
        self.assertSetEqual(set(self.correct_main_domains_list), set(main_domains_list))

    def test_final_domains_lists(self):
        self.assertSetEqual(set(self.correct_final_domain_list), set(final_domains_list))

    def test_domains_to_split_lists(self):
        self.assertSetEqual(set(self.correct_domains_to_split_list), set(domains_to_split_list))


if __name__ == '__main__':
    unittest.main()
