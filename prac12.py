# Print the multiplication table of a number n.
while (True):
    num = int(input("Enter the number to see multiplication table: "))
    i = 1
    while i <= 10:
        result = num * i
        print(num, "*", i ,"=", result )
        i += 1

    print("Program end")
