import sys

def add(num1, num2):
    sum = num1 + num2
    print('{} + {} = {}'.format(num1, num2, sum))

def sub(num1, num2):
    sum = num1 - num2
    print('{} - {} = {}'.format(num1, num2, sum))

def mult(num1, num2):
    sum = num1 * num2
    print('{} * {} = {}'.format(num1, num2, sum))

def div(num1, num2):
    sum = num1 / num2
    print('{} / {} = {}'.format(num1, num2, sum))

def calculate():
    num1 = int(input ('First number: '))
    num2 = int(input ('Second number: '))
    operator = input("Type 'add' to add, 'subtract' to subtract and so on: ")
    if operator  == 'add':
        add(num1, num2)

    elif operator == 'subtract':
        sub(num1, num2)

    elif operator == 'multiply':
        mult(num1, num2)

    elif operator == 'divide':
        div(num1, num2)

calculate()
quit = input('Type \'quit\' to quit and \'continue\' to continue: ')

while quit.lower() != 'quit':
    calculate()
    quit = ''
    quit = input('Type \'quit\' to quit and \'continue\' to continue: ')
    if quit.lower() != 'quit' and quit.lower() != 'continue':
        sys.exit('Invalid Command')

    elif quit.lower() == 'quit':
        sys.exit('Saving Results')

    elif quit.lower() == 'continue':
        calculate()
        quit = ''
        quit = input('Type \'quit\' to quit and \'continue\' to continue: ')

    sys.exit('Saving Results')
