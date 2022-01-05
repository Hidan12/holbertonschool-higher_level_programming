#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    tam = len(my_list)
    if (idx >= tam or idx < 0):
        return(my_list)
    else:
        temp = my_list[idx]
        my_list.remove(temp)
        return(my_list)
