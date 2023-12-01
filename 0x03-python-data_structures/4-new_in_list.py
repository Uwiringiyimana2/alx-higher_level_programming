#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """replaces an element in list without modifying orginal list.

    Args:
        my_list: orginal list
        idx: index
        element: to be placed

    Return:
        modified list
        orginal list if idx is negative or out of range
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    list_copy = my_list.copy()

    list_copy[idx] = element

    return list_copy
