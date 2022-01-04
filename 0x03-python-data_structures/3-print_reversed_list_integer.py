#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = 0
    if my_list is not None:
        for a in range(len(my_list)):
            if (a == 0):
                print("{:d}".format(my_list[-1]))
            else:
                print("{:d}".format(my_list[-(a + 1)]))
