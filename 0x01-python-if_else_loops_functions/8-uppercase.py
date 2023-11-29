#!/usr/bin/python3
def uppercase(str):
    """uppercase prints str in uppercase"""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - ord('a') + ord('A'))
        print("{}".format(c), end="")
