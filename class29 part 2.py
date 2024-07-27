#Guessing Game 2
from random import randint
while (True):
    guessNumber = int(input("Enter your Guess between 1 to 5: "))
    randomNumber = randint(1,5)
    print("Randon number is: ", randomNumber)

    if guessNumber == randomNumber:
        print("You have WON! :)")
    else:
        print("You have lost :( ")
