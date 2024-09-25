# Loop1 
#for i in range(10):
#    print(i)

colors = ["yellow", "red", "pink", "blue"]

for x in colors:
    print(x)

print("*************************************************************************************************************")

str = "vrushali"

for char in str:
    if(char == "l"):
        break
    print(char)
else:
    print("Loop ends here!")

print("*************************************************************************************************************")

nums = (1, 2, 3, 4, 5)

for num in nums:
    print(num)
else:                                   # optional else statement
    print("End of 'nums' tuple")