#!/usr/bin/env python3
'''yes yes yo'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''concatene a string and the square of 
    an int/float and return a tuple with those elements'''
    return (k, v ** 2)
