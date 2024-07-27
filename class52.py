# Use of Constructors
class Student:
    roll = ""
    gpa = ""

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

rahul = Student(11001, 3.75)
rahul.display()

rodela = Student(12175, 3.99)
rodela.display()