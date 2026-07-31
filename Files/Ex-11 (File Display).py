#Program For Accepting Any File Name And Display It's Content
def Display():
    try:
        print("Program Started")
        filename=input("Enter File Name: ")
        with open(filename,"r") as fp:
            filedata=fp.read()
            print(filedata)
    except FileNotFoundError:
        print("\t File Does Not Exist")
#Main Program
Display()
