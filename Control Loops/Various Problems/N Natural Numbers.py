#program for Finding product of N Natural Nums
n=int(input("Enter Any Natural Number: "))
if n<=0:
    print("Invalid Input")
else:
    p=1
    for i in range(1,n+1):
        print("\t {}".format(i))
        p=p*i
    else:
        print("\t product={}".format(p))



