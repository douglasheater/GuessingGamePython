#Douglas Heater
#CIS261
#GuessingGame

import math 
import random
from venv import create

print("Guess the number!")

def play_game():
    limit = int(input("\nEnter the limit: "))

    x = random.randint(1, limit)
    print("I'm thinking of a number from 1 to", limit)

    count = 0 
    while count < limit:
        count += 1
        guess = int(input("\nYour guess: "))
        if x == guess:
            print("The correct number was", x)
            print("You guessed it in", count, "tries")
            break
        elif x > guess:
            print("Too low")
        elif x < guess:
            print("Too high")   

playAgain = "y"
while playAgain.lower() == "y":

    play_game()
    
    playAgain = input("\nWould you like to play again? (y/n): ")
    while playAgain.lower() not in ["y", "n"]:
        playAgain = input("Invalid value: Enter y or n: ")    

            

