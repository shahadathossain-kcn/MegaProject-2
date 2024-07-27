#

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hell():
        print("hello")

    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("hi", self.name, "your avg score is : ", sum/3)

s1 = Student("SHAHADAT", [96,97,98])
print(s1.name, s1.marks)

s1.get_avg()

s1.name = "spiderman"
s1.get_avg()
s1.hell()



