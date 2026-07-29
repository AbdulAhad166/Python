#Program for Finding the Sum of N Natural Nums
n=int(input("Enter How Many Natural Numbers Do You Want: "))
if n<=0:
    print("Invalid Input")
else:
    print("Natural Numbers of {}".format(n))
    s=0
    for i in range(1,n+1):
        print("\t {}".format(i))
        s=s+i
    else:
        print("Sum of {}".format(s))