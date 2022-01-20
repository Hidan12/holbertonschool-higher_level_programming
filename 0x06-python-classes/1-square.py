#!/usr/bin/python3
"""Script that assigns a private instance attribute size to class
    Square"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0):
        if (size >= 0):
            self._size = size
