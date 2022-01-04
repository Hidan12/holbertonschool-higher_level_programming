#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    tam = len(my_list)
    if (idx >= tam or idx < 0):
        return(my_list)
    else:
        my_list[idx] = element
        return(my_list)
