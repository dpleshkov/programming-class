from person import Person

#The 'gender' parameter is filled with True/False rather than Male/Female
#Since there are only two genders (for this exercise transgender is not included) booleans make more sense

kabir = Person("Kabir", False, 15, 5, 8, "dark blue")
kabir.greet()
kabir.show_age()
print("I am {} feet and {} inches tall".format(kabir.feet, kabir.inches))
print("My favorite color is {}\n".format(kabir.fav_color))

people = [
    Person("Kabir", False, 15, 5, 8, "dark blue"),
    Person("Dmitry", False, 15, 6, 1, "brown"),
    Person("Sidd", False, 15, 5, 9, "purple"),
    Person("Vibhav", False, 15, 6, 1, "turquoise"),
    Person("Avani", True, 15, 4, 11, "yellow")
]

for person in people:
    person.greet()
    person.show_age()
    print("I am {} feet and {} inches tall".format(person.feet, person.inches))
    print("My favorite color is {}".format(person.fav_color))
    if person.gender == True:
        print("I am female\n")
    else:
        print("I am male\n")

while True:
    action = input("Add person or quit? ").lower()

    while action == 'add':
        name = input("Enter person's name: ")
        gender = input("Enter person's gender (True for female, False for male)")
        if gender == 'true':
            gender = True
        elif gender == "false":
            gender = False
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
