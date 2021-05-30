#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    return sum(tuple(a * b for a, b in my_list))/sum(x[1] for x in my_list)
