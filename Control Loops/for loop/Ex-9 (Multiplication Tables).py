#program for generating Mul Table for Given Number
n=int(input("Enter Any Number: "))
if n<=0:
    print("Invalid Input")
else:
    print("Multiplication Table For {}".format(n))
    for i in range(1,11):
        print("\t {} x {} = {}".format(n,i,n*i))
