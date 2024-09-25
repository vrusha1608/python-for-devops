# Create Account class with 2 attributes - balance & account No
# Create methods for debit, credit & printing the balance

class Account:

    
    def __init__(self, balance, accNo):
        self.balance = balance
        self.accNo = accNo

    def debit(self, amt):
        self.balance -= amt
        print("Current Balance in Account:", self.accNo, "is:", self.balance)

    def credit(self, amt):
        self.balance += amt
        print("Current Balance in Account:", self.accNo, "is:", self.balance)

    def printBalance(self):
        print("Balance in Account:", self.accNo, "is:", self.balance)


a1 = Account(5000, 100001)
a1.printBalance()
a1.debit(3000)
a1.credit(6000)

