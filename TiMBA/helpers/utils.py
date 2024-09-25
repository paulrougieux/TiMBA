import numpy as np
import pandas as pd
from functools import wraps

from TiMBA.parameters.Defines import VarNames
from TiMBA.parameters.Domains import Domains
from TiMBA.data_management.DataContainer import DataContainer
from TiMBA.parameters.domain_specifiers.AbstractDomainSpecifier import DomainSpecifier
from TiMBA.parameters.domain_lists import (main_domains_list, final_domains_list, domains_to_split_list,
                                           domains_to_align_list, domains_to_optimize_list, domains_to_update_list,
                                           drop_description_domains_list)

from typing import Callable, Any, Tuple, Optional, Union, List, Type
from warnings import warn


def decorate_domain_iteration(domains_list: list) -> Callable:
    """
    Iterates over a given set of domains and returns wrapped function
    :param domains_list: A list of Domains
    """
    def iter_domains(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for domain in domains_list:
                yield func(domain, *args, **kwargs)
        return wrapper
    return iter_domains


def get_domain(domain: DomainSpecifier) -> Optional[Any]:
    return domain


def get_domain_name(domain: DomainSpecifier) -> Optional[Any]:
    try:
        return str(domain)
    except AttributeError:
        return None


def get_domain_start_index(domain: DomainSpecifier) -> Optional[Tuple[Any, Any]]:
    try:
        return str(domain), domain.content_start_index
    except AttributeError:
        return None, None


def get_domain_splitting(domain: DomainSpecifier) -> Optional[Tuple[Any, Any]]:
    try:
        return str(domain), domain.domain_split_list
    except AttributeError:
        return None, None


def get_domain_header(domain: DomainSpecifier) -> Optional[Tuple[Any, Any]]:
    try:
        return str(domain), domain.header_description
    except AttributeError:
        return None, None


def get_info_slope_intercept_calculation(domain: DomainSpecifier) -> Optional[Tuple[Any, Any, Any, Any]]:
    price_col_name = VarNames.PRICE_COLNAME.value
    quantity_col_name = VarNames.QUANTITY_COLNAME.value
    elast_col_name = VarNames.ELASTICITY_COLNAME.value

    price = domain.price if hasattr(domain, price_col_name) else price_col_name
    quantity = domain.quantity if hasattr(domain, quantity_col_name) else quantity_col_name
    elasticity_price = domain.elasticity_price if hasattr(domain, elast_col_name) else elast_col_name

    return str(domain), price, quantity, elasticity_price


def get_info_vectorize(domain: DomainSpecifier) -> Optional[Tuple[Any, Any, Any, Any, Any, Any]]:
    price_col_name = VarNames.PRICE_COLNAME.value
    quantity_col_name = VarNames.QUANTITY_COLNAME.value
    elast_col_name = VarNames.ELASTICITY_COLNAME.value
    slope_col_name = VarNames.SLOPE_COLNAME.value
    intercept_col_name = VarNames.INTERCEPT_COLNAME.value

    price = domain.price if hasattr(domain, price_col_name) else price_col_name
    quantity = domain.quantity if hasattr(domain, quantity_col_name) else quantity_col_name
    elasticity_price = domain.elasticity_price if hasattr(domain, elast_col_name) else elast_col_name
    slope = domain.slope if hasattr(domain, slope_col_name) else slope_col_name
    intercept = domain.intercept if hasattr(domain, intercept_col_name) else intercept_col_name

    return str(domain), price, quantity, elasticity_price, slope, intercept


def extract_results(domain: DomainSpecifier) -> Optional[Tuple[str, Any, Any, Any]]:
    price_col_name = VarNames.PRICE_COLNAME.value
    quantity_col_name = VarNames.QUANTITY_COLNAME.value
    elast_col_name = VarNames.ELASTICITY_COLNAME.value

    quantity = domain.quantity if hasattr(domain, quantity_col_name) else quantity_col_name
    price = domain.price if hasattr(domain, price_col_name) else price_col_name
    elasticity_price = domain.elasticity_price if hasattr(domain, elast_col_name) else elast_col_name

    return str(domain), quantity, price, elasticity_price


class DomainIterator:
    MAIN_DOMAINS = main_domains_list
    FINAL_DOMAINS = final_domains_list
    DESCRIPTION_DOMAINS = drop_description_domains_list
    SPLIT_DOMAINS = domains_to_split_list
    ALIGN_DOMAINS = domains_to_align_list
    OPTIMIZATION_DOMAINS = domains_to_optimize_list
    UPDATE_DOMAINS = domains_to_update_list

    @staticmethod
    def get_domain_names(domains_list):
        return decorate_domain_iteration(domains_list)(get_domain_name)()

    @staticmethod
    def get_domain_start_index(domains_list):
        return decorate_domain_iteration(domains_list)(get_domain_start_index)()

    @staticmethod
    def get_domain_header(domains_list):
        return decorate_domain_iteration(domains_list)(get_domain_header)()

    @staticmethod
    def get_domain_splitting(domains_list):
        return decorate_domain_iteration(domains_list)(get_domain_splitting)()

    @staticmethod
    def get_domain(domains_list):
        return decorate_domain_iteration(domains_list)(get_domain)()

    @staticmethod
    def get_info_slope_intercept_calculation(domains_list):
        return decorate_domain_iteration(domains_list)(get_info_slope_intercept_calculation)()

    @staticmethod
    def get_info_vectorize(domains_list):
        return decorate_domain_iteration(domains_list)(get_info_vectorize)()

    @staticmethod
    def extract_results(domains_list):
        return decorate_domain_iteration(domains_list)(extract_results)()


def mask_data(Data: DataContainer, column_index: int, mask_condition: str, axis: int) -> pd.DataFrame:
    """
    Method to split the content for sheets from world.xlsx with different
    attributes (Manufacture, Transportation, ExogChange)
    :param Data: Datacontainer to split by mask
    :param column_index: Determines on which column of pd.DataFrame masking happens
    :param mask_condition: Condition to split on.
    :param axis: 0 for rows, 1 for columns
    :return: filtered subset
    """
    if axis not in [0, 1]:
        raise ValueError(f"Splitting on axis {axis} not possible. Chose 0 for columns, 1 for row based filtering.")
    subset = Data.data.copy()
    if axis == 0:
        mask = subset.iloc[:, column_index] == mask_condition
    else:
        if type(mask_condition) in (str, int):
            mask_condition = [mask_condition]
        mask = mask_condition
    subset = subset[mask].reset_index(drop=True)
    subset.dropna(inplace=True, axis=0, how="all")
    return subset


def create_help_vectors(
        list_vectors: List[Union[pd.DataFrame, pd.Series, np.ndarray]],
        dtype: Optional[Type[Union[pd.DataFrame, pd.Series, np.ndarray]]] = None,
        allow_mixed_dtype: bool = False, axis: int = 0, drop_idx: bool = True,
) -> Union[pd.Series, pd.DataFrame]:
    """
    Helper function to generate concatenated vectors for TiMBA computation
    :param list_vectors: List of input vectors to be concatenated
    :param allow_mixed_dtype: Boolean, if you want to allow concatenation of different dtypes
    :param dtype: Must be specified if 'allow_mixed_dtype' is False
    :param axis: Axis on which concatenation is performed. 0 for rows, 1 for columns
    :param drop_idx: Index gets resetted by default, you can choose if you want to keep the index of origin by setting
        to True
    :return: Concatenated pd.Series or pd.DataFrame
    """
    accepted_types = [pd.DataFrame, pd.Series, np.ndarray]
    error_msg = f"Type of element in 'list_vectors' at position"
    if not allow_mixed_dtype and dtype is None:
        raise ValueError(f"dtype must be specified if allow_mixed_dtype is False.")
    if not allow_mixed_dtype:
        for i, vec in enumerate(list_vectors):
            if not isinstance(vec, dtype):
                raise TypeError(f"{error_msg} {i}: {type(vec)} != defined type: {dtype}.")
    else:
        dim_1_shape = list(map(lambda x: x.shape[0], list_vectors))
        dim_2_shape = list(map(lambda x: x.shape[1] if len(x.shape) > 1 else None, list_vectors))
        if len(set(dim_2_shape)) == 1 and list(set(dim_2_shape))[0] is None:
            pass  # Pass for those with data on only one axis
        else:
            if (not len(set(dim_1_shape)) in (0, 1)) or (not len(set(dim_2_shape)) in (0, 1)):
                warn(f"Input vectors in 'list_vectors' with unequal shapes/ndims: Shape-Dim:0: {dim_1_shape}, "
                     f"Shape-Dim:1: {dim_2_shape}", )
        input_list = list_vectors.copy()
        for i, vec in enumerate(input_list):
            if type(vec) in accepted_types:
                if isinstance(vec, np.ndarray):
                    if len(vec.shape) == 1:
                        list_vectors[i] = pd.Series(vec)
                    else:
                        list_vectors[i] = pd.DataFrame(vec)
                else:
                    pass
            else:
                raise TypeError(f"{error_msg} {i}: {type(vec)}. Accepted types are: {accepted_types}.")
    return pd.concat(list_vectors, axis=axis).reset_index(drop=drop_idx)
