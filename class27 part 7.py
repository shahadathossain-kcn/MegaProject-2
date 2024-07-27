# Check Factorial Number

num = int(input("Enter any number: "))

x = range(2,num)

"""
print(x)
y = list(x)
print(y)
"""

for i in x:
    if num % i == 0:
        print("Not prime")
    else:
        print("Prime")