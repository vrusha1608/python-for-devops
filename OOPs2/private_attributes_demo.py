# program for private attributes of class

class Account:

    def __init__(self, accNo, accPassw):
        self.accNo = accNo
        self.__accPassw = accPassw      # declared as private attribute with __ in beginning ...e.g __accPassw

    def reset_password(self):
        print(self.__accPassw)

    
account1 = Account("10001", "Pass@123")

print(account1.accNo)
# print(account1.accPassw)    #not encouraged to print sensitive information

print(account1.reset_password())


