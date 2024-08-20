#!/usr/bin/env python3
'''simple index helper func'''


def index_range(page: int, page_size: int) -> tuple:
    '''
    simple helper function that return the range
    of an index
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
