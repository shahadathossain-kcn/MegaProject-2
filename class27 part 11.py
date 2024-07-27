# LCM finding:
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

maximum = max(a, b)
while (True):
    if (maximum % a == 0) and (maximum % b == 0):
        break
    maximum = maximum + 1
print(f"The LCM of {a} and {b} is {maximum}")
