#Program For Renaming Folder---os.rename()
import os
try:
    os.rename("BB","Hyderabad")
    print("Folder Renamed---Verify")
except FileNotFoundError:
    print("Folder Does Not Exist")
