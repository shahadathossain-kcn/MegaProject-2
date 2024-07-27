# Pattern
"""
n = 3
*
***
*****
"""
n = int(input("Enter any number: "))
x = range(n+1)
for i in x:
    print((2*i-1) * "*")