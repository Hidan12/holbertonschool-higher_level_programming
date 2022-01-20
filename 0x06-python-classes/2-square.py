#!/usr/bin/python3
"""Script that assigns a private instance attribute size to class
    Square with size validation"""
class Square:
    def __init__(self, size=0):
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
