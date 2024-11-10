# list out files of each folder in user input

import os

folders = input("Enter list of folders here:").split(" ")

for folder in folders:
    print("====================Files in folder",folder,"are :- ============================================")
    files = os.listdir(folder)
    for file in files:
        print(file)