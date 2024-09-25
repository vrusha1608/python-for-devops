# Search for a number x in this tuple using for loop
(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 71

for i in tup:
    if(x==i):
        print("found ..")
        break
    i+=1
else:
    print("not found ..")