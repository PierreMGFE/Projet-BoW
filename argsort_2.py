import numpy as np


def argsort(l1):
    """
    :param l1: list ;
    :return sorting: argsort, indexes such as " l1[sorting] = l1_sorted" ;
    :return l1_sorted: l1 sorted ;
    """
    if not l1:
        return [],[]
    l1_array = np.array(l1)
    sorting = np.argsort(l1_array)
    l1_sorted = list(l1_array[sorting])
    return sorting, l1_sorted

