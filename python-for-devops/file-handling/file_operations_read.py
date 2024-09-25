# Basic operations of file 

# file path ==> C:\Users\vrush\OneDrive\Documents\python-for-devops\file-handling\demo.txt

f = open("C:/Users/vrush/OneDrive/Documents/python-for-devops/file-handling/demo.txt", "r") 

# data = f.read()
# print(data)

# print(type(data))

print("*****************************************************************************************************************")

line1 = f.readline()    # cursor is ending at end of line (end of line is '\n' ...so it is printing new line at the end)
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)    # it will print new line because file is read completely already

f.close()   #closing the file





