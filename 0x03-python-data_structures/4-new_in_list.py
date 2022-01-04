#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tam = len(my_list)
    a = 0
    new = []
    if (idx >= tam or idx < 0):
        return(my_list)
    else:
        for a in range(tam):
            if(a != idx):
                new.append(my_list[a])
            else:
                new.append(element)
        return (new)
