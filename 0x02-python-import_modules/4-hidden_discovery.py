#!/usr/bin/python3
if __name__ == "__main__":
    ''' prints all the names defined by the compiled module hidden_4.pyc'''
    import hidden_4

    names = dir(hidden_4)
    for n in names:
        if n[:2] != "__":  # check if the name does not start with 2 underscore
            print(n)
