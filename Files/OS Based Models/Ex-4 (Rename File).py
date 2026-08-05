#Program For Renaming File---os.rename()
import os
try:
    os.rename("FileName.Extension","NewFileName.Extension")
    print("File Renamed---Verify")
except FileNotFoundError:
    print("File Does Not Exist")
