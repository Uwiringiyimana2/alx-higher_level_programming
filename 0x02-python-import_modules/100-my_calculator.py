#!/usr/bin/python3
# 100-my_calculator.py

if __name__ == "__main__":
    """my calculator handles basic operations"""
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = sys.argv[1]
    operator = sys.argv[2]
    b = sys.argv[3]
    operator = ['+', '-', '*', '/']
    if sys.argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if sys.argv[2] == operator[0]:
        print("{} + {} = {}".format(a, b, add(int(a), int(b))))
    elif sys.argv[2] == operator[1]:
        print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
    elif sys.argv[2] == operator[2]:
        print("{} * {} = {}".format(a, b, mul(int(a), int(b))))
    elif sys.argv[2] == operator[3]:
        print("{} / {} = {}".format(a, b, div(int(a), int(b))))
