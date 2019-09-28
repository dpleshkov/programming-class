#Imports python's "random" library which allows you to choose a random number
import random

#Selects random number and establishes how many guesses you have
number = random.choice(range(0, 100))
guesses_left = 10

#Prompts the user to guess a number - if they don't choose an actual number the computer will make them redo it
try:
    print("\n{} guesses left".format(guesses_left))
    guess = int(input("Guess a number (between 1 and 100): "))
except ValueError:
    guess = int(input("Not a number, please try again: "))

#Game loop - continues until the game ends
while guess != number:

    if guess > number:
        try:
            guesses_left -= 1
            print("\n{} guesses left".format(guesses_left))
            guess = int(input("Number is smaller, try again: "))
        except ValueError:
            guess = int(input("Not a number, please try again: "))
            
    if guess < number:
        try:
            guesses_left -= 1
            print("\n{} guesses left".format(guesses_left))
            guess = int(input("Number is larger, try again: "))
        except ValueError:
            guess = int(input("Not a number, please try again: "))

    #If you run out of guesses, you lose
    if guesses_left == 0:
        print("Sorry, you are out of guesses. The number was {}".format(number))
        break
            
#If you win the game
if guess == number and guesses_left >= 0:
    print("Great job! You guessed the number with {} guesses left!".format(guesses_left))
