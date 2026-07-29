#Program for Generating Mul Tables for random Dynamic values
n=int(input("Enter Any Number: "))
if n<=0:
    print("Invalid Input")
else:
    lst=[]
    for i in range(1,n+1):
        val=int(input("Enter {} value:".format(i)))
        lst.append(val)
    else:
        print("List of Values: ",lst)
        for num in lst:
            if num<=0:
                print("Invalid Input")
            else:
                print("Multiplication Table for {}".format(num))
                for i in range(1,11):
                    print("{} x {} = {}".format(num,i,i*num))
            print("------------------------------------------------")
