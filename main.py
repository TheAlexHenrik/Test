import math
import numpy as np
print("Hello")


class Shape:
    colour = "blue"
    filled = True

    def __init__(self, colour, filled):
        self.colour = colour
        self.filled = filled

    def getColour(self):
        return self.colour

    def isFilled(self):
        return self.filled

    def setColour(self, colour):
        self.colour = colour

    def setFilled(self, filled):
        self.filled = filled


class Circle(Shape):
    radius = 1

    def __init__(self, radius, colour, filled):
        self.radius = radius
        super().__init__(colour, filled)

    def getArea(self):
        return self.radius * self.radius * math.pi

    def getPeri(self):
        return self.radius * 2 * math.pi

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius


circle1 = Circle(10, "Blue", True)
circle2 = Circle(2, "Red", False)
print(circle1.getArea())
print(circle1.getPeri())
print(circle1.getColour())
print(circle1.isFilled())
print(circle2.getColour())
print(circle2.getPeri())

arr = np.array([1,2,3,4,5,6])

print(arr[:4])