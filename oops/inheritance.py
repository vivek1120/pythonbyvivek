class shape:
    def area(self):
        return 0
    
class rectangular(shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width


class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius **2)
    
    
shape = shape()

rectangular = rectangular(5,4)
circle = circle(9)

print("this is the rectangular length : ",rectangular.length)
print(rectangular.area())
print(circle.area())

setattr(rectangular,'length',9)

print("this is the rectangular changed length : ",rectangular.length)

print(rectangular.area())




