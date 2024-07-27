'''
x = int(input("Enter any number: "))
if x>10:
    if x>20:
        print("Hi")
    else:
        print("Hello")
'''

num1 = int(input("Enter any number 1: "))
num2 = int(input("Enter any number 2: "))
num3 = int(input("Enter any number 3: "))

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)