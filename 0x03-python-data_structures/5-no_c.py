#!/usr/bin/env python3
def no_c(my_string):
    new = []
    if my_string is not None:
        for a in my_string:
            if (a != 'c' and a != 'C'):
                new.append(a)
        return(new)
