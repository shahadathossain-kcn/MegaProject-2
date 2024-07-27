# factorial number
n = int(input("Enter any number: "))
y = range(1, n+1, 1)
print(y)
z = list(y)
print(z)
sum = 1
for x in y:
    sum = sum * x

print(sum)
