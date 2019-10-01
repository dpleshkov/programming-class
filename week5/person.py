class Person:

    def __init__(self, name, age, height, fav_color):
        self.name = name
        self.age = age
        self.height = height
        self.fav_color = fav_color

    def greet(self):
        print("Hi, my name is {}".format(self.name))

    def show_age(self):
        print("I am {} years old. In 1 year, I will be {} years old".format(self.age, self.age + 1))
