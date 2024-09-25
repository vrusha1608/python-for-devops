# WAF that replaces all occurences of "java" with "python" in "practice.txt"

with open("C:/Users/vrush/OneDrive/Documents/python-for-devops/file-handling/practice.txt","r") as f:
    data = f.read()
    newData = data.replace("Java","Python")
    print(newData)

with open("C:/Users/vrush/OneDrive/Documents/python-for-devops/file-handling/practice.txt","w") as f:
    f.write(newData)