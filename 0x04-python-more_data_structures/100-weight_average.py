#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        numerator = 0
        denumerator = 0
        for element in my_list:
            numerator += element[0] * element[1]
            denumerator += element[1]
        return numerator / denumerator
