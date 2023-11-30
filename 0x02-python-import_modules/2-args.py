#!/usr/bin/python3
# 2-args.py

if __name__ == "__main__":
    """Prints the number of and the list of its arguments"""
    from sys import argv

    num_args = len(argv) - 1
    singular_plural = "argument" if num_args == 1 else "arguments"
    ending = "." if num_args == 0 else ":"

    print("{} {}{}".format(num_args, singular_plural, ending))

    for i in range(num_args):
        print("{} : {}".format(i + 1, argv[i + 1]))
