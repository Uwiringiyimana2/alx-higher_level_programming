#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """prints all integers of list in reverse order

    Args:
        my_list: list
    """
    count = len(my_list) - 1
    for n in range(len(my_list)):
        print("{}".format(my_list[count - n]))
