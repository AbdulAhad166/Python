#Program for Generating All Even Numbers in Reverse Even Numbers
n=int(input("Enter How Many Even Numbers Do You Want in Range: "))
if n<=0:
    print("Invalid Input")
else:
    print("Even Numbers Reversed")
    i=n
    while i>=1:
        if i%2==0:
            print("\t {}".format(i))
        i=i-1