class Person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name

p1 = Person()
p1.changeName("potassium cyanide")
print(p1.name)
print(Person.name)
