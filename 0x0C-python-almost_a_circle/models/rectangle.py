#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):

    """Rectangle class"""

    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):

        """Iniciatation method"""

        self.width = width
        self.height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def get_width(self):
        return(self.__width)

    @width.setter
    def width(self, width):

        """width setter"""

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):

        """height setter"""

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def get_height(self):
        return(self.__height)

    @set_x.setter
    def set_x(self, x):

        """x setter"""

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def get_x(self):
        return(self.__x)

    @set_y.setter
    def set_y(self, y):

        """y setter"""

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def get_y(self):
        return(self.__y)
