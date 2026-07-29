#program for accepting List of Values and Find their sum
n=int(input("Enter Any Number: "))
if n<=0:
    print("Invalid Input")
else:
    lst=[]
    for  i in range(1,n+1):
        val=int(input("Enter {} value: ".format(i)))
        lst.append(val)
    else:
        print("List of values=",lst)
        print("\t Sum={}".format(sum(lst)))
        print("\t Avg={}".format(sum(lst)/len(lst)))