#Program For Generating Multiplication Table
n=int(input("Enter Any Number For Generating Multiplication Table: "))
if n<=0:
    print("Invalid Number")
else:
    print("Multiplication Table For {}".format(n))
    i=1
    while i<11:
        print("\t {} x {} = {}".format(n,i,n*i))
        i=i+1
    else:
        print("Table Completed")