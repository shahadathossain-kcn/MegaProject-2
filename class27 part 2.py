# 2 + 4 + 6 + ... ... ... + n

n = int(input("Enter the last number: "))
sum = 0
x = range(2, n+1, 2)
y = list(x)
print(y)

for z in x:
    sum = sum + z

print(sum)




