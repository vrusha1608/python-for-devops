# Define an Employee class with attributes role, department and salary.This class also has a showDetails() method
# Create an Engineer class that inherits properties from Employee and has additional attributes name & age


class Employee:

    def __init__(self, role, dept, sal):
        self.role = role
        self.dept = dept
        self.sal = sal

    def showDetails(self):
        print("role =>", self.role)
        print("dept =>",self.dept)
        print("sal =>",self.sal)
        print("*****************************************************************************************************************")


e1 = Employee("accountant", "finance", 60000)
e1.showDetails()

class Engineer(Employee):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 120000)

eng1 = Engineer("Vrushali", 27)
eng1.showDetails()