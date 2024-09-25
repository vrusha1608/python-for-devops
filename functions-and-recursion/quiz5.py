# WAF to take input of a number from user and check/print if number is even/ odd

num = int(input("Enter any number:"))

def check_even_or_odd(num):
    res = ""
    if(num%2==0):
        res = "Even"
    else:
        res = "Odd" 
    return res



result = check_even_or_odd(num)

print("Entered number is =>", result)