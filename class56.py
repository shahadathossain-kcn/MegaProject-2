#A practical example of inheritance

class Shape:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print("I'm area method of shape class")

class Tringle(Shape):
    def area(self):
        area = 0.5 * self.base * self.height
        print("Area of triangle =", area)

class Rectangle(Shape):
    def area(self):
        area = self.base * self.height
        print("Area of rectangle =", area)

t1 = Tringle(20, 30)
t1.area()

t2 = Rectangle(10, 20)
t2.area()
