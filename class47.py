"""
num2 = int(input("Enter a number: "))
result = 20 / num2
print(result)
print("Done")
"""
"""
text = "Shahadat"
print(text[9])
print("Done")
"""

# Exception Handling
try:

    list = [20, 0, 30]
    result = list[0] / list[3]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by zero is not possible")
except IndexError:
    print("Index Error")
finally:
    print("successful")
