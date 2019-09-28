#Imports python's "system" library
import sys

#Creates an empty array of shopping items
shopping_list = []

action = input("Type 'add' to add item, 'view' to view list and 'quit' to quit: ").lower()

while action != 'add' and action != "quit" and action != "view":
    action = input("Invalid action, try again: ")

while True:
    if action == "add":
        item = input("What would you like to add? ")
        shopping_list.append(item)
        action = input("Type 'add' to add item, 'view' to view list and 'quit' to quit: ").lower()      

    elif action == "view":
        for item in shopping_list:
            print("- {}".format(item))
        action = input("Type 'add' to add item, 'view' to view list and 'quit' to quit: ").lower()


    elif action == "quit":
        sys.exit("Quitting application")
    
