#!/usr/bin/python3


'''function that returns a tuple with the length
of a string and its first character'''


def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first_char = None
    else:
        first_char = sentence[0]
    
    return length, first_char
