#!/usr/bin/python3
# 3-infinite_add.py

if __name__ == "__main__":
    """Program tha prints the result of the addition of all arguments"""
    import sys

    count = len(sys.argv) - 1
    sum = 0

    for i in range(count):
        sum += int(sys.argv[i + 1])
    print(sum)
