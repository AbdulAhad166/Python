#Program for Accepting Student Details and Save in File as Records
#This Program is for Entering The Student Values in Default
def savestudentdata():
    with open("stud1.data", "a") as fp:
        sno=int(input("Enter Student Number: "))
        name=input("Enter Student Name: ")
        marks=input("Enter Student Marks: ")
        #sno,name,marks are called Objects Resides in Main Memory
        #Save Details in File
        fp.write(str(sno)+"\t")
        fp.write(name+"\t")
        fp.write(str(marks)+"\n")
        print("Student Details Saved in File---Verify")
#Main Program
savestudentdata()
