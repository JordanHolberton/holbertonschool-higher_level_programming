#!/usr/bin/env python3
"""Create class circle"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        """Abstract method for calculating area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for calculating perimeter"""
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        """Calculate the area of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints and returns the area and perimeter of the shape passed.
    
    Arguments:
    shape -- An object of a class that implements the Shape interface
    """
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
    return area, perimeter
