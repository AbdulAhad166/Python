#Program for Opening a file in 'r' mode
try:
    fp=open('stud.data',"r")
except FileNotFoundError:
    print("File Does NOt Exists")
else:
    print("\t File Opened in Read Mode")
    print("\t type of fp=",type(fp))
    print("\t Is File Closed?=",fp.closed)
finally:
    print("Program Executed")
    try:
        fp.close()
    except NameError:
        print("\t File Not Opened At All ----No Need To Close")
    else:
        print("\t If File Closed?= ",fp.closed)