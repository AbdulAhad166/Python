#Program for Deleting a Folder---os.rmdir()
import os
try:
    os.rmdir("NIT")
    print("Folder Deleted---Verify")
except FileNotFoundError:
    print("Folder Does Not Exist")
except OSError:
    print("Ensure That The Deleting Folder Must Be Empty---Check Once")
