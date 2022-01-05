#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div = []
    for a in range(len(my_list)):
        if (my_list[a] % 2):
            div.append(False)
        else:
            div.append(True)
    return (div)
