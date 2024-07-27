"""
Figure out a way to store 9 and 9.0 as seperate values in
the set. ( You can take help of built-in data types.)
"""

#values = {9, "9.0", 9.25, 8, 8.25}
#print(values)

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)