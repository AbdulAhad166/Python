#Program to Generate All Odd Numbers in Reversed Order
n=int(input("Enter Odd Numbers How many You Want in Range: "))
if n<=0:
    print("Invalid Input")
else:
    print("Odd Numbers in Range are")
    i=n
    while i>=1:
        if i%2!=0:
            print("\t {}".format(i))
        i=i-1