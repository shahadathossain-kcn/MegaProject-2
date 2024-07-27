#WAP to find the sum of n numbers. (using while)
"""
n = int(input("enter any number you want a sum : "))

sum = 0
i = 0
while i <= n:
    sum = sum + i
    i += 1
print(sum)
"""

n = int(input("enter any number : "))

sum = 0
for i in range(1, n+1):
    sum = sum + i
print(sum)