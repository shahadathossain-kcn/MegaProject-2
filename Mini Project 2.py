# random password generator
import random
import string

pass_len = 12
charValue = string.ascii_letters + string.digits + string.punctuation

# list comprehension
res = "".join([random.choice(charValue) for i in range(pass_len)])
print(res)
"""
password = ""
for i in range(pass_len):
    password += random.choice(charValue)

print("your random password is : ", password)
"""