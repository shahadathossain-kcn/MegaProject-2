#Exercise
class Tringle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5* self.base * self.height

tringle1 = Tringle(10, 20)
print(tringle1.calculate_area())

t2 = Tringle(20, 30)
print(t2.calculate_area())
