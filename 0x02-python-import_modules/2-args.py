#!/usr/bin/python3
if __name__ == "__main__":
    '''a program that prints the number of and the list of its arguments'''
    import sys
    num_args = len(sys.argv) - 1
    print("{} argument{}{}{}".format(
        num_args,
        's' if num_args != 1 else '',
        '.' if num_args == 0 else '',
        ':' if num_args > 0 else ''
    ))
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
