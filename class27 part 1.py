# 1 + 2 + 3 + 4 + 5 + ............. + n

n = int(input("Enter the last number: "))
sum = 0
y = range(1, n+1, 1)
z = list(y)
print(z)

for x in y:
    sum = sum + x
print(sum)