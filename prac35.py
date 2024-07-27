class Student:
    college_name = "ABC college"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("you are welcome", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Shahadat", 80)
print(s1.name, s1.marks)

s1.welcome()

print(s1.get_marks())