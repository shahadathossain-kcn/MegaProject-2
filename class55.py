# Method Overriding
class Phone:
    def __init__(self):
        print("I'm in phone class.")

class Samsung(Phone):
    def __init__(self):
        super().__init__()
        print("I'm is Samsung Class")

x = Samsung()
