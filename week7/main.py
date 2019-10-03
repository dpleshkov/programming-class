#We are going to simulate a classroom

from teacher import Teacher
from student import Student
from furniture import Furniture
from stationery import Stationery
from book import Book

#Dictionary stores all the info about math class
math_classroom = {
    "teacher": Teacher("Mr. Brad", False, 14, 14, 14, "teacher", "math"),
    "textbooks": [Book("UCSMP Pre-Algebra", "Transitions I-II", 600, True), Book("UCSMP Algebra", "Algebra I", 650, True), Book("UCSMP Geometry", "Geometry", 700, True), Book("UCSMP Advanced Algebra", "Algebra II", 750, True)],
    "stationery": [Stationery("ruler", 12, "blue", 10, "measuring"), Stationery("pencil", 8, "yellow", 25, "writing"), Stationery("eraser", 2, "pink", 20, "erasing"), Stationery("protractor", 10, "transparent", 10, "measuring angles"), Stationery("compass", 6, "black", 5, "drawing circles"), Stationery("graph paper", 20, "yellowish", 75, "being written on")],
    "furniture": (Furniture("table", 5, 4, "wood", 4), Furniture("chair", 3, 4, "metal", 12), Furniture("whiteboard", 7, 6, "plastic", 2)),
    "students": [
        Student("Mallika", True, 14, 5, 1, 9, 'student') 
    ]
}
    
print("{} is our {} teacher".format(math_classroom['teacher'].name, math_classroom['teacher'].subject))
math_classroom['teacher'].teach()
print('\n')
    
for textbook in math_classroom['textbooks']:
    print("Our textbook for {} is {} - it has {} pages".format(textbook.topic, textbook.title, textbook.pages))

print('')
for item in math_classroom['stationery']:
    print("\nWe have {} {} {}s".format(item.quantity, item.color, item.name))
    item.work()
    
print("\n\nWe have the following items of furniture: ")
for object in math_classroom['furniture']:
    print(" - {} {}s".format(object.quantity, object.name))
    
print("\n\nSo far, we have {} student(s). They are the following: ".format(len(math_classroom['students'])))
for student in math_classroom['students']:
    print(" - {}, who is in grade {}".format(student.name, student.grade))