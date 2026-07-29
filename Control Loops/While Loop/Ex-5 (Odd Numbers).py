#Program for Generating All Odd Numbers
n=int(input("Enter How Many Odd Numbers Do You Want in Range: "))
if n<=0:
    print("Invalid Input")
else:
    print("Odd Numbers in Range are")
    i=1
    while i<=n:
        if i%2!=0:
            print("\t {} ".format(i))
        i=i+1
