# basic file operations ==> write operation

f = open("C:/Users/vrush/OneDrive/Documents/python-for-devops/file-handling/demo.txt", "a+") 

f.write("\nthis is new line appending inside file")   #it will append at the end of file

# check in file if data is appended or not

# f = open("C:/Users/vrush/OneDrive/Documents/python-for-devops/file-handling/demo.txt", "w+") 

# f.write("We are overriding file contents with 'w' file mode")





#f = open("C:/Users/vrush/OneDrive/Documents/python-for-devops/file-handling/demo.txt", "r") 

print(f.read())