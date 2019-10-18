import sys

definitions = {
    'potato': 'a brown root vegetable',
    'water': 'A liquid which living things need to survive',
    'teacher': 'a person who teaches things',
    'earth': 'the world as we know it'
}

action = input("Add, search or quit? ").lower()

while action not in ('add', 'search', 'quit'):
    action = input("Invalid action, try again: ")
    
while action == "add":
    word = input("What word do you want to add? ")
    definition = input("What is the word's definition? ")
    definitions[word] = definition
    action = input("\nAdd, search or quit? ").lower()
    
while action == "search":
    word = input("What word do you want to look up? ")
    while word not in definitions:
        word = input("Word not in dictionary, try again: ")
    if word in definitions:
        print(definitions[word])
        action = input("\nAdd, search or quit? ").lower()
        
if action == "quit":
    sys.exit("Exiting app")