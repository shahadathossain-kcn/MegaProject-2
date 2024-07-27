# 2*2 + 4*4 + 6*6 + ... ... ... + n*n

n = int(input("Enter the last nubmer: "))
sum = 0
x = range(2, n+1, 2)
print(x)
y = list(x)
print(y)

for z in x:
    sum = sum + z*z

print(sum)
