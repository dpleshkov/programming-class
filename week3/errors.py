#Targets Value Errors
def value_error():
    number = input("Enter a number: ")

    try:
        number = int(number)
        return number
    except ValueError:
        number = input("Not a valid number, try again: ")

#Targets ZeroDivision Errors
def zero_division_error():
    number1 = value_error()
    number2 = value_error()
    try:
        quotient = number1/number2
        print(quotient)
    except ZeroDivisionError:
        number2 = int(input("Cannot divide by 0, try again: "))
        quotient = number1/number2
        print(quotient)

#Targets Index Errors
def index_error(array):
    index = int(input("Enter index you want to access: "))
    try:
        print(array[index])
    except IndexError:
        index = int(input("Index not in array, try again: "))
        print(array[index])
        

print(value_error())
zero_division_error()
index_error([1, 2, 3, 4])