#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return
    bool_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list
