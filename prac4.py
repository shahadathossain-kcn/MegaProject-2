""" WAP  to check if a list contains
a palindrome of elements (Hint: use copy() method)
"""

list1 = []
list1.append(int(input("Enter a number: ")))
list1.append(int(input("Enter another number: ")))
list1.append(int(input("Enter the last number: ")))
print(list1)

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("Palindrome")
else:
    print("Not palindrome.")
