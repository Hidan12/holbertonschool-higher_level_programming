#!/usr/bin/python3
def common_elements(set_1, set_2):
    temp_lis = []
    for a in set_1:
        for b in set_2:
            if (a == b):
                temp_lis.append(a)
    return(temp_lis)
