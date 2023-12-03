#!/usr/bin/python3
a = 89
b, c = 10, a
c, a, b = a, b, c
print("a={:d} - b={:d}".format(a, b))
