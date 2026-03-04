import math
class Shape:
    def area(self):
        print("Calculating area...")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print(math.pi*self.radius ** 2)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
    
    def area(self):
        print(self.length*self.width)
        
r=int(input("Enter the radius of the circle: "))
c1=Circle(r)
c1.area()

l=int(input("Enter the length of the rectangle: "))
b=int(input("Enter the breadth of the rectangle: "))
r1=Rectangle(l,b)
r1.area()
