from person import Person

#This class uses inheritance, where it inherits the properties of another class
class Teacher(Person):
    def __init__(self, name, gender, age, feet, inches, profession, subject):
        super().__init__(name, gender, age, feet, inches, profession)
        self.profession = "teacher"
        self.subject = subject
        
    def teach(self):
        print("{} is teaching {}".format(self.name, self.subject))