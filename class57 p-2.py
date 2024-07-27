#Multiple Inheritance

class A:
    def display(self):
        print("I'm inside class A")

class B:
    def display(self):
        print("I'm inside class B")

class C(B, A): # if A is at starting then A will get priority; also same as the 
    # A -> display()
    # B -> display()
    #def display(self):
     #   print("I'm inside class C")
    pass

obl = C()
obl.display()