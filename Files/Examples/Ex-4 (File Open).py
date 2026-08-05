#Program for Opening a File in 'r' Mode
try:
    with open("stud.data1","r") as fp:
        print("\t File Opened in Read Mode")
        print("\t Is File Closed with open()?= ",fp.Closed)  #False
    print("\t Is File Closed After with open()?= ",fp.closed) #True
except FileNotFoundError:
    print("\t File Does Not Exist")