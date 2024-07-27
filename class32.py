# Dictionaries
studentID = {
    "101" : "Shahadat Hossain",
    "102" : "Potassium Cyanide",
    "103" : "Hydrochloric Acid",
    "104" : "Formic Acid",
}
"""print(studentID["101"])"""
x = input("Enter the secret key: ")
print(studentID.get(x, "Not a valid key!"))


