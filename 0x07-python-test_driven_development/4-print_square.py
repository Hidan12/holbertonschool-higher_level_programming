#!/usr/bin/python3
def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size >= 0:
        for a in range(size):
            print("#" * size)
    else:
        raise ValueError("size must be >= 0")
