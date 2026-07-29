#Program for Generating All Even Numbers within 'N'
n=int(input("Enter How many Even Numbers Do You Want in Range: "))
if n<=0:
    print("Invalid Input")
else:
    print("All Even Numbers Are")
    i=1
    while i<=n:
        if i%2==0:
            print("\t {} ".format(i))
        i=i+1