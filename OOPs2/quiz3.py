# Create a class called Order which stores item & its price
# Use dunder function __gt__() to convey that:
# order1>order2 if price of order 1>price of order2

class Order:

    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        if(self.price > order2.price):
            return ("Order1 is greater than Order 2")
        else:
            return ("Order2 is greater than Order 1")


o1 = Order("chips", 20)
o2 = Order("tea",15)

result = o1 > o2

print(result)



    