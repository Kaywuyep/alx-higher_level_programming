#!/usr/python3


'''function that finds all multiples of 2 in a list'''


def divisible_by_2(my_list=[]):
    result = []

    for num in my_list:
        result.append(num % 2 == 0)

    return result
