#Program for CSV File Data by Using File Pointer Whose Type is <class,_io.TextIOWrapper>
with open("stud.csv",'r',newline='') as fp:
    csvdata=fp.read()
    print(csvdata)