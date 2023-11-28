#!/usr/bin/python3
def fizzbuzz():
    """prints the numbers from 1 to 100"""
    for number in range(101):
        if number % 3 == 0:
            print("{}".format('Fizz'), end=" ")
        elif number % 5 == 0:
            print("{}".format('Buzz'), end=" ")
        elif number % 3 == 0 and number % 5 == 0:
            print("{}".format('FizzBuzz'), end=" ")
        else:
            print("{}".format(number), end=" ")
