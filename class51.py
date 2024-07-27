# Introducing Methods
class Student:
    roll = ""
    gpa = ""

    def setValue(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

"""
rahul = Student()
rahul.roll = 11001
rahul.gpa = 3.73
rahul.display()
"""
rahul = Student()
rahul.setValue(11001, 3.75)
rahul.display()
"""
rodela = Student()
rodela.roll = 12175
rodela.gpa = 4.0
rodela.display()
"""
rodela = Student()
rodela.setValue(12175, 3.99)
rodela.display()