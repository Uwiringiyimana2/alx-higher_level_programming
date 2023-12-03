#!/bin/python3
# 2-replace_in_list.py

def replace_in_list(my_list, idx, element):
    """a function that replaces an element of a list at a specific position..

    Args:
        my_list: lists
        idx: index
        element: replaces the element of list

    Return:
        modified list
        orginal list if idx is negative or out of range
    """
    if idx >= 0 or idx <= (len(my_list)):
        my_list[idx] = element
    return my_list
