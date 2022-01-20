#!/usr/bin/python3
"""Script that assigns a private instance attribute size to class
    Square with size validation"""


class Square:
    """Class that defines a square with a private instance attribute size"""

    def __init__(self, size=0):
        if (size >= 0):
            self.__size = size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value=0):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return(int(self.__size) * int(self.__size))
