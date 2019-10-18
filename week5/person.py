class Person:

    def __init__(self, name, gender, age, feet, inches, fav_color):
        self.name = name
        self.gender = gender
        self.age = age
        self.feet = feet
        self.inches = inches
        self.fav_color = fav_color

    def greet(self):
        print("Hi, my name is {}".format(self.name))

    def show_age(self):
        print("I am {} years old. In 1 year, I will be {} years old".format(self.age, self.age + 1))
