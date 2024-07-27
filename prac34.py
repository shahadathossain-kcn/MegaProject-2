# OOPS 1
class Student:
    college_name = "ABC College"
    name = "anonymous" # class attr
    # default constructors
    def __init__(self):
        print("Adding new student in data base...")
        pass
    # parameterized constructors
    def __init__(self, name, marks):
        self.name = name # obj attr > class attr
        self.marks = marks
        print("Adding new student in data base...")

s1 = Student("Hossain", 99)
print(s1.name , s1.marks)

s2 = Student("Shahadat", 100)
print(s2.name, s2.marks)

print(s2.college_name) #or
# print(Student.college_name)

"""
print(s1.name)
s2 = Student()
print(s2.name)
"""
"""
class Car:
    color = "blue"
    model = "gtp 85"

car1 = Car()
print(car1.color)

car2 = Car()
print(car2.model)
"""