#!/usr/bin/env python3
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''add all elements of an input list that 
    can be composed of ints and/or floats'''
    return sum(mxd_lst)
