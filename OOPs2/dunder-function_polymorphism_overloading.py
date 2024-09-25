#Basic program on Operator Overloading - Dunder Functions

# Program for arithmetic operations on complex number i.e. ai+bj

class ComplexNumber:

    def __init__(self, real, img) :
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, " i +",self.img, " j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return ComplexNumber(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return ComplexNumber(newReal, newImg)

num1 = ComplexNumber(1,3)
num2 = ComplexNumber(2,7)

num1.showNumber()
num2.showNumber()

# addition = num1.add(num2) 
# instead of calling function we can use "+" operator to add complex number using dunder function

addition = num1 + num2
addition.showNumber()

sub = num1 - num2
sub.showNumber()