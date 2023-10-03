#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str  # Return the original string if index is out of bounds
    return str[:n] + str[n+1:]
