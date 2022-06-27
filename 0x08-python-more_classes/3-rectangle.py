#!/usr/bin/python3
# 3-rectangle.py
"""Define a class Rectangle."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, size=0):
        """Initialize a new square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
