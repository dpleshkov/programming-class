#Imports python's "system" library
import sys

#Functions to add, subtract, multiply and divide
def add(num1, num2):
    sum = num1 + num2
    print('{} + {} = {}'.format(num1, num2, sum))

def subtract(num1, num2):
    difference = num1 - num2
    print('{} - {} = {}'.format(num1, num2, difference))

def multiply(num1, num2):
    product = num1 * num2
    print('{} * {} = {}'.format(num1, num2, product))

def divide(num1, num2):
    quotient = num1 / num2
    print('{} / {} = {}'.format(num1, num2, quotient))

#Calculate function performs all operators on given numbers
def calculate():
    num1 = int(input ('\nFirst number: '))
    num2 = int(input ('Second number: '))
    operator = input("Type 'add' to add, 'subtract' to subtract and so on: ").lower()
    
    while operator not in ('add', 'subtract', 'multiply', 'divide'):
        operator = input("Invalid operator, try again: ").lower()
        
    if operator  == 'add':
        add(num1, num2)

    elif operator == 'subtract':
        subtract(num1, num2)

    elif operator == 'multiply':
        multiply(num1, num2)

    elif operator == 'divide':
        divide(num1, num2)

#Runs until user quits the application
calculate()
quit = input('Type \'quit\' to quit and \'continue\' to continue: ')

while quit.lower() != 'quit':
    calculate()
    quit = ''
    quit = input('Type \'quit\' to quit and \'continue\' to continue: ')
    if quit.lower() != 'quit' and quit.lower() != 'continue':
        sys.exit('Invalid Command')

    elif quit.lower() == 'quit':
        sys.exit('Exiting')

    elif quit.lower() == 'continue':
        calculate()
        quit = ''
        quit = input('Type \'quit\' to quit and \'continue\' to continue: ')

    sys.exit('Exiting')
