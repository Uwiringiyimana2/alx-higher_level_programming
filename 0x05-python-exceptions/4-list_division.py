#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0]*list_length
    for i in range(list_length):
        num1 = my_list_1[i]
        num2 = my_list_2[i]
        division = 0

        try:
            division = num1 / num2
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list[i] = division
    return (new_list)
