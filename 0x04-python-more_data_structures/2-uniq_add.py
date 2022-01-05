#!/usr/bin/python3
def uniq_add(my_list=[]):
    temp_lis = list(set(my_list))
    add = 0
    for a in range(len(temp_lis)):
        add += temp_lis[a]
    return (add)
