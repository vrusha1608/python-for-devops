# Create Student class that takes name, marks of 3 subjects as argument in constructor
# Then create a method to print the average.

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average_marks(self):
        avg = (self.marks[0] + self.marks[1] + self.marks[2])/3
        return avg
    
s1 = Student("Vrushali", [95, 95, 95])
s2 = Student("Karan", [97, 56, 78])
s3 = Student("Sneha", [76,59,39])

print("Average Marks of", s1.name, "is", s1.calculate_average_marks()) 

print("Average Marks of", s2.name, "is", s2.calculate_average_marks()) 

s1.name = "Striver"
print(s1.calculate_average_marks())





