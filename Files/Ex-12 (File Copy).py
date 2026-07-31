#Program For Copying The Content of One File into Another File
def FileCopy():
    try:
        srcfile=input("Enter Source File: ") #Here we can give path also as Source file
        with open(srcfile,"r") as sp:
            dstfile=input("Enter Destination File: ") #Here we can give path also as Destination file
            with open(dstfile,"a") as dp:
                #read the source file data
                srcfiledata=sp.read()
                #write the source file data to destination file data
                dp.write(srcfiledata)
                print("1 File(s) Copied---Verify")
    except FileNotFoundError:
        print("\t File Does Not Exist")
#Main Program
FileCopy()



