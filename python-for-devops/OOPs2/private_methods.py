# Program for private attributes & methods


class Person:
    __name = "Anonymous"

    def __hello(self):
        print("Hello Person!")

    def welcome(self):
        self.__hello()


p1 = Person()
#p1.__hello()            # Can not access private method --> AttributeError: 'Person' object has no attribute '__hello'

#Accessing private method using public method
p1.welcome()    