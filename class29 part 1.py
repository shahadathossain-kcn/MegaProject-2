#Guessing Game 1
from random import randint
for x in range(10): # here range means the total game will be replayed for 10 times
    guessNumber = int(input("Enter your Guess between 1 to 5: "))
    randomNumber = randint(1,5)
    print(randomNumber)

    if guessNumber == randomNumber:
        print("You have WON! :)")
    else:
        print("You have lost :( ")
