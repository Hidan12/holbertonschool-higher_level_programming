#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for a in range(len(my_list)):
        if (my_list[a] != search):
            new.append(my_list[a])
        else:
            new.append(replace)
    return(new)
