#Program for Listing the Folder Data Present in folder in file-------listdir()
import os
try:
    FolderName=input("Enter Folder Name in List Files: ")
    filelist=os.listdir(FolderName)
    print("List of Files: ")
    for filename in filelist:
        print(filename)
except FileNotFoundError:
    print("Folder Does Not Exist")