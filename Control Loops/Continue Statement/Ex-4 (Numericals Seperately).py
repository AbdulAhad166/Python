#Program for accepting List of Numerical values
# and Get Separately + Vals and -VE VCals
n=int(input("Enter How Many Numbers You Want: "))
if n<=0:
    print("Invalid Input")
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter {} value:".format(i)))
        lst.append(val)
    else:
        print("\t List of Values: ",lst)
        pslist=[]
        for val in lst:
            if val<=0:
                continue
            pslist.append(val)
        else:
            print("\t List of +ve values: ",pslist)
            nslist=[]
            for val in lst:
                if val>=0:
                    continue
                nslist.append(val)
            else:
                print("\t List of -ve values: ",nslist)

