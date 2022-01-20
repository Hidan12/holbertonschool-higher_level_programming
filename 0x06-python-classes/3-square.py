#!/usr/bin/python3
"""Script that assigns a private instance attribute size to class
    Square with size validation"""


class Square:
    """Class that defines a square with a private instance attribute size"""
    def __init__(self, size=0):
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return(int(self.__size) * int(self.__size))
