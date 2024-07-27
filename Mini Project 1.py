import random

randNum = random.randint(1, 100)

while True:
    userChoice = input("guess the number or Quit(Q) : ")
    if (userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if (userChoice == randNum):
        print("Success: Correct Guess!!")
        break
    elif (userChoice < randNum):
        print("your number was too small. take a bigger guess...")
    else:
        print("your number was too big. take a smaller guess...")


print("____GAME OVER____")
