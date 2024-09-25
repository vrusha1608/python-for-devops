# Basic concepts of class and object and constructor in python

# creating class

class Student:

    college_name = "GECA"       #class attribute
    name = "ABC"                #class attribute

    #default
    def __init__(self): # type: ignore
        pass

    #parametrised
    def __init__(self, name, marks):
        self.name = name  #obj attr
        self.marks = marks
        print("adding new student in to the database")
        print(self)

#creating object (instance)

s1 = Student("Vrushali Potdar", 97)
print(s1.name, s1.marks, Student.college_name)

s2 = Student("Karan H", 78)
print(s2.name, s2.marks, Student.college_name)