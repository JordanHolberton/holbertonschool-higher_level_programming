#!/usr/bin/env python3
"""Module for Shape, Circle, and Rectangle classes with area and perimeter calculations."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class representing a generic shape."""
    
    @abstractmethod
    def area(self):
        """Abstract method for calculating the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for calculating the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle, inherits from Shape."""
    
    def __init__(self, radius):
        """Initialize the circle with a radius."""
        if radius <= 0:
            raise ValueError("Radius must be greater than 0.")
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle, inherits from Shape."""
    
    def __init__(self, width, height):
        """Initialize the rectangle with a width and height."""
        if width <= 0 or height <= 0:
            raise ValueError("Width and Height must be greater than 0.")
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints and returns the area and perimeter of the shape passed.
    
    Arguments:
    shape -- An object of a class that implements the Shape interface
    """
    area = shape.area()
    perimeter = shape.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
    return area, perimeter
