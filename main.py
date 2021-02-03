import math

print("Hello")


class Circle:
    radius = 0

    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return self.radius * self.radius * math.pi

    def getPeri(self):
        return self.radius * 2 * math.pi

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius


circle1 = Circle(10)
print(circle1.getArea())
print(circle1.getPeri())
circle1.setRadius(1)
print(circle1.getArea())

list = ["Banan", "Apple", "Orange"]

list.append("Lort")

print(list)

list.remove("Banan")

print(list)