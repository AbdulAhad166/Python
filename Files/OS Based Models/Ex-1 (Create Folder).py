#Program for Creating a Folder---os.mkdir
import os
try:
    os.mkdir("BB")
    print("Folder Created---Verify")
except FileExistsError:
    print("Folder Already Exists")
except FileNotFoundError:
    print("Root Folder Not Created")  #Here If a Folder is created in that you need to add
    # new file/folder then first you need to create a folder then only yu can create a new folder inside a folder
