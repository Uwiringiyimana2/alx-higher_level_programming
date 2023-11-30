#!/usr/bin/python3
# 2-args.py

if __name__ == "__main__":
    """Prints the number of and the list of its arguments"""
    import sys

    number = len(sys.argv) - 1

    if number == 0:
        print("0 arguments.")
    elif number == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number))

    if number > 0:
        for n in range(number):
            print("{} : {}".format(n + 1, sys.argv[n + 1]))
