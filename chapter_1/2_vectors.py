import math

"""
A class to represent and perform simple operations on 2D vectors.
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)
    
    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    """
    Without custom __repr__ for objects, it would display a vector instance and
    the memory address. The string returned by __repr should be unambiguous and
    match the source code necessary to recreate the object. A good rule of thumb
    is making it look like calling the constructor of the class. __str__ should
    return a string suitable for user readability.
    """
    def __repr__(self):
        # with !r, calls repr on val before formatting, string coords display with quotes
        return f"Vector({self.x!r}, {self.y!r})"  

