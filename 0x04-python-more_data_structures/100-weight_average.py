#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple(<score>, <weight>)"""
    if not my_list:
        return 0
    sum_product = sum(score * weight for score, weight in my_list)
    sum_weights = sum(weight for _, weight in my_list)

    if sum_weights == 0:
        return 0

    return sum_product / sum_weights
