#Program for Generating 1 to N Mul Tables
n=int(input("Enter Any Number: "))
if n<=0:
    print("Invalid Input")
else:
    for i in range(1,n+1):
        print("Multiplication Table for {}".format(i))
        print("-----------------------------------------")
        for j in range(1,11):
            print("{} x {} = {}".format(i,j,i*j))
        else:
            print("-----------------------------------------")