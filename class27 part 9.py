# GCD/ HCF finding:

def findHCF (x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range (1, smaller + 1):
        if (x%i == 0 ) and (y%i == 0):
            hcf = i
    return hcf
x = int(input("Enter a number: "))
y = int(input("Enter another nubmer: "))
print("The hcf of the given two numbers is " , findHCF(x, y))