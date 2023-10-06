#!/usr/bin/python3


'''function that adds 2 tuples'''


def add_tuple(tuple_a=(), tuple_b=()):
    # If a tuple is smaller than 2, use the value 0 for each missing integer
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # If a tuple is bigger than 2, use only the first 2 integers
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    
    return result
