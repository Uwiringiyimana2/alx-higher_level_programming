#!/usr/bin/python3
"""writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns
    the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        w_num = f.write(text)
        return w_num
