
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter anothe one number: "))

if num1>num2 and num1>num3:
    print("Maximum number is " , num1)

elif num2 > num1 and num2 > num3:
    print("Maximum number is " ,num2)

else:
    print("Maximum number is " , num3)