#!/usr/bin/python3
def common_elements(set_1, set_2):
    temp_lis = []
    temp1 = sorted(set_1)
    temp2 = sorted(set_2)
    for a in temp1:
        for b in temp2:
            if (a == b):
                temp_lis.append(a)
                break
    return(temp_lis)
