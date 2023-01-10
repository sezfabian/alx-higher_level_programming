#!/usr/bin/python3
def max_integer(my_list=[]):
    m = 0
    if not my_list:
        return None
    else:
        for i in range(len(my_list)):
            if my_list[i] < m:
                m = my_list[i]
        for i in range(len(my_list)):
            if my_list[i] > m:
                m = my_list[i]
        return m
