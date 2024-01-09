#!/usr/bin/python3
"""appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and
        returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        num = f.write(text)
        return num
