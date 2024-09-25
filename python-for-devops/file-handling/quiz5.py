# From a file containing numbers separated by comma, print the count of even numbers


with open("C:/Users/vrush/OneDrive/Documents/python-for-devops/file-handling/nums.txt","w") as f:
    f.write("23,87,86,81,26,24,29,8,12,15,1,7,16,14,86,43,12,1,89")

with open("C:/Users/vrush/OneDrive/Documents/python-for-devops/file-handling/nums.txt", "r") as f:
    data = f.read()
    nums = data.split(",")
    count=0
    for i in nums:
        if(int(i) %2 == 0):
            count += 1
    
    print("Count of even numbers in file =>", count)