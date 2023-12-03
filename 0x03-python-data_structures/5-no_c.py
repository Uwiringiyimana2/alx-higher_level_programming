#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """removes all characters c and C from a string.

    Args:
        my_string: string to remove cC

    Return:
        the new string
    """
    new_string = ""
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return new_string
