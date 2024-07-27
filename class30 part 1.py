# List as input from user
n = input("Enter a text of numbers: ")
list = n.split()
sum = 0
print(list)

for num in list:
    sum = sum + int(num)

print(sum)
