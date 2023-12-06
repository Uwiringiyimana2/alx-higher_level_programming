#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_dict = sorted(a_dictionary)
    for i in my_dict:
        print("{}: {}".format(i, a_dictionary[i]))
