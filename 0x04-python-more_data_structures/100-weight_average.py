#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    result2 = 0
    result3 = 0
    for item in my_list:
        result1 = item[0] * item[1]
        result2 += result1
        result3 += item[1]
    result4 = result2/result3
    return result4
