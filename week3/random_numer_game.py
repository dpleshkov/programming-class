#Imports python's "random" library which allows you to choose a random number
import random

#Selects random number and establishes how many guesses you have
number = random.choice(range(0, 100))
guesses_left = 10
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

#Prompts the user to guess a number - if they don't choose an actual number the computer will make them redo it
print("\n{} guesses left".format(guesses_left))
guess = input("Guess a number (between 1 and 100): ")
is_not_number = False
for letter in guess:
    if letter not in numbers:
        is_not_number = True
        break
if is_not_number == False:
    guess = int(guess)
else:
    while is_not_number == True:
        guess = input("Not a number, try again: ")
        is_not_number2 = False
        for letter in guess:
            if letter not in numbers:
                is_not_number2 = True
                break
        if is_not_number2 == False:
            is_not_number = False
    
if is_not_number == False:
    guess = int(guess)

#Game loop - continues until the game ends
while guess != number:
    
    if guess > number:
        guesses_left -= 1
        print("\n{} guesses left".format(guesses_left))
        guess = input("Number is smaller, try again: ")
        for letter in guess:
            if letter not in numbers:
                is_not_number = True
                break
        if is_not_number == False:
            guess = int(guess)
        else:
            while is_not_number == True:
                guess = input("Not a number, try again: ")
                is_not_number2 = False
                for letter in guess:
                    if letter not in numbers:
                        is_not_number2 = True
                        break
                if is_not_number2 == False:
                    is_not_number = False
    
        if is_not_number == False:
            guess = int(guess)

            
    if guess < number:
        guesses_left -= 1
        print("\n{} guesses left".format(guesses_left))

        guess = input("Number is larger, try again: ")
        for letter in guess:
            if letter not in numbers:
                is_not_number = True
                break
        if is_not_number == False:
            guess = int(guess)
        else:
            while is_not_number == True:
                guess = input("Not a number, try again: ")
                is_not_number2 = False
                for letter in guess:
                    if letter not in numbers:
                        is_not_number2 = True
                        break
                if is_not_number2 == False:
                    is_not_number = False
    
        if is_not_number == False:
            guess = int(guess)

    #If you run out of guesses, you lose
    if guesses_left == 0:
        print("Sorry, you are out of guesses. The number was {}".format(number))
        break
            
#If you win the game
if guess == number and guesses_left >= 0:
    print("Great job! You guessed the number with {} guesses left!".format(guesses_left))
