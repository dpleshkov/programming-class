from person import Person

kabir = Person("Kabir", 15, 5.8, "dark blue")
kabir.greet()
kabir.show_age()
print("I am {} feet tall".format(kabir.height))
print("My favorite color is {}\n".format(kabir.fav_color))

people = [
    Person("Kabir", 15, 5.8, "dark blue"),
    Person("Dmitry", 15, 5.11, "..."),
    Person("Sidd", 15, 5.9, "purple"),
]

for person in people:
    person.greet()
    person.show_age()
    print("I am {} feet tall".format(person.height))
    print("My favorite color is {}\n".format(person.fav_color))

while True:
    action = input("Add person or quit? ").lower()

    while action == 'add':
        name = input("Enter person's name: ")
        age = int(input("Enter person's age: "))
        height = input("Enter person's height: ")
        fav_color = input("Enter person's favorite color: ")
        people.append(Person(name, age, height, fav_color))

        for person in people:
            person.greet()
            person.show_age()
            print("I am {} feet tall".format(person.height))
            print("My favorite color is {}\n".format(person.fav_color))

        action = input("\nAdd person or quit? ").lower()
    if action == 'quit':
        break
