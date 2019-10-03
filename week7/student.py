from person import Person

#This class uses inheritance, where it inherits the properties from another class
class Student(Person):
    def __init__(self, name, gender, age, feet, inches, grade, profession):
        super().__init__(name, gender, age, feet, inches, profession)
        self.profession = "student"
        self.grade = grade