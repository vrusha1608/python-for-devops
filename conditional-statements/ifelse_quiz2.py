# WAP to find the greatest of 3 numbers entered by user

firstNum = int(input("Enter first number:"))
secondNum = int(input("Enter second number:"))
thirdNum = int(input("Enter third number:"))

if(firstNum>=secondNum and firstNum>=thirdNum):
    print(firstNum,"is the greatest number!")
elif(secondNum>=firstNum and secondNum>=thirdNum):
    print(secondNum,"is the greatest number!")
else:
    print(thirdNum,"is the greatest number!")