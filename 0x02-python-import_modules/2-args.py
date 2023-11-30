#!/usr/bin/python3
# 2-args.py

if __name__ == "__main__":
    """Prints the number of and the list of its arguments"""
    import sys

    number = len(sys.argv) - 1
    args = sys.argv

    if number == 0:
        print("0 arguments.")
    elif number == 1:
        print("{} argument:".format(number))
    else:
        print("{} arguments:".format(number))

    if number > 0:
        for n in range(number):
            print("{} : {}".format(n + 1, args[n + 1]))
