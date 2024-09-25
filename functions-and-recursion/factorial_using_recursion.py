# WAP to find fatorial using recursion

def find_factorial(num):
    if(num==0 or num==1):
        return 1
    else:
        return num*find_factorial(num-1)
    
factorial = find_factorial(4)

print("Factorial is=>", factorial)
