#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """prints all integers of list in reverse order

    Args:
        my_list: list
    """
    if my_list:
        for n in reversed(range(len(my_list))):
            print("{:d}".format(my_list[n]))
