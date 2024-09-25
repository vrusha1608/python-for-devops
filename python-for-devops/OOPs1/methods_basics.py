# Basic program on methods 


class Student:

    #default
    def __init__(self, name, city): # type: ignore
        self.name = name
        self.city = city

    def print_hello(self):
        print("Hello", self.name)

    @staticmethod
    def print_welcome():
        print("Welcome")

Student.print_welcome()     # invoking global method
    
s1 = Student("Vrushali", "Sangli")
s1.print_hello()

del s1.name #deleting attribute
#print(s1.name)

print(s1.city)

del s1   # deleting object

#print(s1)


