# basic demo class for abstraction

class Car:

    def __init__(self):
        self.accelerator = False
        self.brake = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.brake = True
        print("car started ..")

c1 = Car()
c1.start()