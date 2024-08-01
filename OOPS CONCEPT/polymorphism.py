class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class Square(Shape):
    def __init__(self,side_length):
        self.side_length=side_length
    def area(self):
        return self.side_length**2
circle=Circle(5)
square=Square(4)
print(f"Area of circle:{circle.area()}")
print(f"Area of square:{square.area()}")
