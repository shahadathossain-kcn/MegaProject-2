#WAP to find the factorial of first n numbers. (using for)

n = int(input("enter number : "))

fact = 1
i = 1

"""
while i <= n:
    fact *= i
    i += 1
print("factorial is = ", fact)
"""

for i in range(1, n+1):
    fact *= i
print("factorial is = ", fact)
