
numofletters = 0
numofwords = 0
numofdigits = 0

text = input("Enter a text of number: ") # My name is 123

for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numofletters = numofletters + 1
    elif x >= '0' and x <= '9':
        numofdigits = numofdigits + 1
    elif x == ' ':
        numofwords = numofwords + 1

print("Number of letters: ", numofletters)
print("Number of words: ", numofwords+1)
print("Number of Digits: ", numofdigits)
