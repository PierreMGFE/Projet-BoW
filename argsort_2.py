import numpy as np


def argsort(l1):
    if not l1:
        return ValueError('Liste vide')
    l1_array = np.array(l1)
    sorting = np.argsort(l1_array)
    l1_sorted = list(l1_array[sorting])
    return sorting, l1_sorted

