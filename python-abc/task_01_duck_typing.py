#!/usr/bin/python3
"""Shapes, Interfaces, and Duck Typing"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract Shape class"""

    @abstractmethod
    def area(self):
        """Calculate area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter"""
        pass


class Circle(Shape):
    """Circle class"""

    def __init__(self, radius):
        """Initialize circle"""
        self.radius = radius

    def area(self):
        """Return area of circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return perimeter of circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """Return area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape information"""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
