#Program for Demonstrating How To Open File and Knowing About Different Modes and Files
try:
    with open("C:\\Users\\dell\\PycharmProjects\\Python\\Files\\stud2.data","x+") as fp:
        print("Type of fp= ",type(fp))
        print("\t Is File Closed?= ",fp.closed)
        print("\t File Name= ",fp.name)
        print("\t File Mode= ",fp.mode)
        print("\t Is File Closed?= ",fp.closed)
        print("\t Is File Readable?= ",fp.readable())
        print("\t Is File Writable?= ",fp.writable())
    print("\t Is File Closed?= ",fp.closed)
except FileExistsError:
    print("\t File Name Exists")