#!/usr/bin/env python3
'''Annotate the below functions parameters and return
values with the appropriate types'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''take an iterable list as input and return a list of tuple'''
    return [(i, len(i)) for i in lst]
