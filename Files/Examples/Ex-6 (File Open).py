#Program for Demonstrating How to Open Files and Knowing about Different Properties of Modes
#and Files
with open("C:\\Users\\dell\\PycharmProjects\\Python\\Files\\Stud1.data","a+") as fp:
    print("\t Type of fp= ",type(fp))
    print("\t Is File Closed?= ",fp.closed)
    print("\t File Name= ",fp.name)
    print("\t File Mode= ",fp.mode)
    print("\t Is File Readable?= ",fp.readable())
    print("\t Is File Writable?= ",fp.writable())
print("\t Is File Closed?= ",fp.closed)

