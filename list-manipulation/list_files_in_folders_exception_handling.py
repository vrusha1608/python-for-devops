# list out files of each folder in user input

import os

folders = input("Enter list of folders here:").split(" ")

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide valid folder name, looks like found does not exists ....")
    except PermissionError:
        print("No access to this folder", folder)

        print("====================Files in folder",folder,"are :- ============================================")
        for file in files:
            print(file)