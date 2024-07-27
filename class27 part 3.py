# 1*1 + 2*2 + 3*3 + ... ... ... + n*n = ?

sum = 0
n = int(input("Enter the last number: "))
x = range(1, n+1, 1)

for z in x:
    sum = sum + z*z

print(sum)