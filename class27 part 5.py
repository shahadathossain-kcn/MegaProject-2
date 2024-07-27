# 1 + 1/2 + 1/3 + ... ... ... + 1/n

n = int(input("Enter the last number: "))
sum = 0.0
x = range(1, n+1, 1)
print(x)
y = list(x)
print(y)

for z in x:
    sum = sum + 1/z
print(sum)
