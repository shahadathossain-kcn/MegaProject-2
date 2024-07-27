# Abstraction -> Hierarchical Inheritance
from abc import ABC, abstractmethod
# we cannot make any object from which class we used "@abstractmethod"
class Shape(ABC):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @abstractmethod
    def area(self):
        pass

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
