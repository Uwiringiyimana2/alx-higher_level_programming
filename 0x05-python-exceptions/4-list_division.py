#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0]*list_length
    for i in range(list_length):
        try:
            num1 = float(my_list_1[i])
            num2 = float(my_list_2[i])

            division = num1 / num2
        except (TypeError, ValueError):
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            new_list[i] = division
    return (new_list)
