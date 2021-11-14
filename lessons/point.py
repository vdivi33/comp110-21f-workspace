"""Example of a point Class"""
from __future__ import annotations

class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a Point with its x, y components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        """Mutates: multiplies components by factor"""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point:
        """Immutable: multiplies compnents by factor without mutation."""
        return Point(self.x * factor, self.y * factor)

    def __str__(self) -> str:
        """Produce a str representtion of a point for humans."""
        return f"{self.x}, {self.y}"
    
    def __repr__(self) -> str:
        """"Produce a str representation of a point for Python!"""
        return f"Point({self.x}, {self.y})"

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * float."""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, rhs: Point) -> Point:
        print("__add__ was called")
        return Point(self.x + rhs.x, self.y + rhs.y)

a: Point = Point(1.0, 2.0)
b: Point = a * 2.0
print(a + b)
print(a) 
print(b)