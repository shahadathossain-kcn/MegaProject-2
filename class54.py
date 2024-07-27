#Inheritance
class Phone: # Parent Class
    def call(self):
        print("You can call.")

    def message(self):
        print("You can message.")

class Samsung(Phone): # Child Class
    # call, message
    def photo(self):
        print("You can take a photo.")

p = Phone()
p.call()
p.message()

s = Samsung()
s.call()
s.message()
s.photo()
print(issubclass(Samsung, Phone))
print(issubclass(Phone, Samsung))
