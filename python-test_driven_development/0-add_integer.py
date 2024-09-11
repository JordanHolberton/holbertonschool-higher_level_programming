#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    Adds two integers a and b. If b is not provided, it defaults to 98.
    a and b must be integers or floats. If not, a TypeError is raised.
    Floats are cast to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
