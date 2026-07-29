#Program for Generating All Odd Numbers till N and using only for loop
n=int(input("Enter How Many Odd Numbers Do You Want: "))
if n<=0:
    print("Invalid Input")
else:
    print("Odd Numbers within {}".format(n))
    for i in range(1,n+2,2):
        print("\t {}".format(i))
    else:
        print("Program Executed")