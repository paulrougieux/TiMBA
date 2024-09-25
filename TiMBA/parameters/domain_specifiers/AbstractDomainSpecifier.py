from abc import ABC, abstractmethod


class DomainNameSpecifier:

    def __repr__(self):
        return repr(self.__class__.__name__)

    def __str__(self):
        return self.__class__.__name__


class MainDomainSpecifier(ABC):

    @property
    @abstractmethod
    def content_start_index(self):
        pass


class RegionCodeSpecifier(ABC):

    @property
    @abstractmethod
    def region_code(self):
        pass


class CommodityCodeSpecifier(ABC):

    @property
    @abstractmethod
    def commodity_code(self):
        pass


class FinalDomainSpecifier(ABC):

    @property
    @abstractmethod
    def header_description(self):
        pass


class SubDomainSpecifier(ABC):

    @property
    @abstractmethod
    def splitting_mask(self):
        pass

    @property
    @abstractmethod
    def column_index(self):
        pass

    @property
    @abstractmethod
    def mask_axis(self):
        pass


class SplitDomainSpecifier(ABC):

    @property
    @abstractmethod
    def domain_split_list(self):
        pass


class DomainSpecifier(DomainNameSpecifier, MainDomainSpecifier, RegionCodeSpecifier, CommodityCodeSpecifier,
                      FinalDomainSpecifier, SubDomainSpecifier, SplitDomainSpecifier, ABC):
    pass
