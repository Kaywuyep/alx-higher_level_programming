#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """ divides element by element 2 lists"""
    result = []
    for i in range(list_length):
        try:
            # Try to perform division
            a = my_list_1[i]
            b = my_list_2[i]

            div_result = a / b
            result.append(div_result)

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)

        except TypeError:
            print("wrong type")
            result.append(0)

        except IndexError:
            print("out of range")
            result.append(0)

        finally:
            # Clean up
            pass

    return result
