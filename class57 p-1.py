# Types of Inheritance
#Multi_level Inheritance

class A:
    def display1(self):
        print("I'm inside class A")

class B(A):
    def display2(self):
        print("I'm inside class B")

class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("I'm inside class C")

#p1 = C()
#p1.display1()
#p1.display2()
#p1.display3()

#p2 = B()
#p2.display1()
#p2.display2()

#p3 = A()
#p3.display1()

p1 = C()
p1.display3()