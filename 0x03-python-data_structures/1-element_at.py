#!/usr/bin/python3
# 1-element_at.py

def element_at(my_list, idx):
    """function that retrieves an element from a list like in C

    Args:
        my_list: lists
        idx: index

    Return:
        None if idx is negative or out of range
    """
    for i in my_list:
        if idx < 0 or idx > (len(my_list) - 1):
            return None
        else:
            return my_list[idx]
