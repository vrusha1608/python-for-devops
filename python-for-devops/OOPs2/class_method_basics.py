# Basic program for classmethod

class Person:

    name = "anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name


    # def changeName(self, name):
    #     self.name = name

# 2 ways to change value of class attribute 'name'
#     def changeName(self, name):
#         Person.name = name      # solution1
#         self.__class__.name = name      # solution2




p1 = Person()
p1.changeName("Vrushali Potdar")
print(p1.name)

print(Person.name)