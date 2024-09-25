# WAP to find factorial of a number using for loop

num = 5
fact=1

for i in range(num,1,-1) :
    fact*=i

print("Factorial of",num,"is",fact)