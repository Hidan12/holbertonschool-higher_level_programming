#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    temp_lis = []
    bol = True
    for a in set_1:
        for b in set_2:
            if (a == b):
                bol = False
                break
        if (bol):
            temp_lis.append(a)
        bol = True
    for a in set_2:
        for b in set_1:
            if (a == b):
                bol = False
                break
        if (bol):
            temp_lis.append(a)
        bol = True
    return(temp_lis)
