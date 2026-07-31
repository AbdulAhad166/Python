#program for Demonstrating How to Open the File
#and Knowing about Different Properties of Modes and Files
try:
    with open("Stud.data","r+") as fp:
        print("\t Type of fp= ",type(fp))
        print("\t Is File is Closed?= ",fp.closed)
        print("\t File Name= ",fp.name)
        print("\t File Mode= ",fp.mode)
        print("\t Is File Readable?= ",fp.readable())
        print("\t Is File Writable?= ",fp.writable())
    print("\t Is File Closed?= ",fp.closed)
except FileNotFoundError:
    print("\t File Does Not Exist")
