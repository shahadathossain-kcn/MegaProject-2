"""
input marks

80-100 = A+
70-79 = A
60-69 = A-
"""

marks = int(input("Enter your marks: "))

'''
if marks > 80 or marks == 80:
    print("Your result is A+")
elif marks > 70 or marks == 79:
    print("Your result is A")
elif marks > 60 or marks == 69:
    print("Your result is A-")

else:
    print("Passed")
'''

'''
if marks >= 80 and marks <= 100:
    print("Your result is A+")
if marks >= 70 and marks <= 7975:
    print("Your result is A")
'''
if 80 <= marks <= 100:
    print("A+")
elif 70 <= marks <= 79:
    print("A")
elif 60 <= marks <= 69:
    print("A-")
