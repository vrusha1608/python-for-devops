# Search if the word "learning" exists in the file or not


word = "learning"


with open("C:/Users/vrush/OneDrive/Documents/python-for-devops/file-handling/practice.txt", "r") as f:
    data = f.read()
    
    if (data.find(word) != -1):
        print("found!")
    else:
        print("not found!")
