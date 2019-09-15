# Using conditionals (if-then statements) in Python

age = int(input("How old are you? > ")) # variable age equals the input converted into an integer

if age >= 18: # if age is greater than or equal to 18:
    print("You are an adult")

if age <= 19 and age >= 13: # if age is less than or equal to 19 and age is greater than or equal to 13:
    print("You are a teenager")

elif age < 13: # else: if age is less than 13:
    print("You are a child")