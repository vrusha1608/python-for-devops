# Program on @property decorator

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((phy+chem+math)/3) + "%"

    # Any changes in value of attribute will reflect in property attribute as well
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + " %"

s1 = Student(98,97,99)

print(s1.percentage) #percentage is  not a method .....it is property/ attribute of class

s1.math = 86  #updating marks of one subject

print(s1.percentage)        # printing older value of percentage