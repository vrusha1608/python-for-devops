# Program for understanding of break and continue keywords

i=1

while i<=5:
    print(i)
    if(i==3):
        break
    i+=1

print("end of loop")


print("************************************************************************************************")

i=1

while i<=5:
    if(i==3):
        i+=1
        continue    #skip the below statements
    print(i)
    i+=1
