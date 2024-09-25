# program on multi level inheritance

class Car:

    @staticmethod
    def start():
        print("car started ..")

    @staticmethod
    def stop():
        print("car stopped ..")


class ToyotaCar(Car):

    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type


car1 = Fortuner("Diesel")
car2 = Fortuner("Petrol")

print(car2.start())     #Accessing base/ parent class's method 
