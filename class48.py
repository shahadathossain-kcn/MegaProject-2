# Exception Handling
"""
try:
    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(result)
except (ValueError, ZeroDivisionError):
    print("You have entered incorrect input")
finally:
    print("Thanks!")
"""


def voter(age):
    if age < 18:
        raise ValueError("Underage voter.")
    return "YOU are allowed to vote"

try:
    #print(voter(19))
    print(voter(16))
except ValueError as e:
    print(e)
