# Basic program of functions in Python


def print_hello():
    print("hello")

print_hello()

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

def sum(a,b):       #function definition
    sum=a+b
    return sum

sum = sum(a,b) #function call with arguments

print("Sum of",a,"and",b,"is=>", sum)