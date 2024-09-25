# Search for number x in this tuple using loop:
[1, 4, 9, 16, 25, 36, 49,64, 81, 100]


x = int(input("Enter number to search:"))

tup = (1, 4, 9, 16, 25, 36, 49,64, 81, 100)

i=0

while i<len(tup):
    if(x==tup[i]):
        print("found at index = ",i)
        break
    i+=1

