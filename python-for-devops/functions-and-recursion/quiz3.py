# WAF to find the factorial of number n

def find_factorial(num):
    fact=1
    for i in range(num,1,-1):
        fact*=i
    return fact

fact = find_factorial(4)

print("Factorial is=>", fact)
    