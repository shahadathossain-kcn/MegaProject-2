# Classes & Objects
class Student:
    roll = ""
    gpa = ""
rahul = Student()
#print(isinstance(rahul, Student))

rahul.roll = 11001
rahul.gpa = 3.73

print(f"Roll: {rahul.roll}, GPA: {rahul.gpa}")

rodela = Student()
rodela.roll = 12175
rodela.gpa = 4.0
print(f"Roll: {rodela.roll}, GPA: {rodela.gpa}")