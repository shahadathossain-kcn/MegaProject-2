"""
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
        # percentage
stu1 = Student(97, 95, 93)
print(stu1.percentage)

stu1.phy = 86
print(stu1.phy)
stu1.calcPercentage()
print(stu1.percentage)


"""


# The above function can be writen easily by using property method.
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    """def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
        # percentage """
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"

stu1 = Student(97, 95, 93)
print(stu1.percentage)

stu1.phy = 86
#stu1.calcPercentage()
print(stu1.percentage)