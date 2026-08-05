#Program for Removing File---os.remove()
import os
try:
    os.remove("C:\\Users\\dell\\PycharmProjects\\Python\\Files\\Examples\\stud2.data")
    print("File Removed---Verify")
except FileNotFoundError:
    print("File Does Not Exist")
