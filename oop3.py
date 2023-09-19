class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    def is_squre(self):
        return self.length == self.width

# Usage:
rect2 = Rectangle(7,7)

print(rect2.area())
print(rect2.perimeter())

print(rect2.is_squre())
