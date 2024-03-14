#!/usr/bin/python3
'''Class Rectangle that inherits from BaseGeometry (7-base_geometry.py)'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class that inherits the BaseGeometry'''

    def __init__(self, width, height):
        '''Initialize the rectangle'''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        '''Return the area of the rectangle'''
        return self.__height * self.__width

    def __str__(self):
        '''Return string representation of Rectangle'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
