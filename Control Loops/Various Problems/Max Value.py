#program for accepting List of Values and Find  Max Element
n=int(input("Enter Any Value: "))
if n<=0:
    print("Invalid Input")
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter {} value: ".format(i)))
        lst.append(val)
    else:
        print("List of values",lst)
        maxelement=lst[0]
        for val in lst[1:]:
            if val>maxelement:
                maxelement=val
        else:
            print("Max Element is ",maxelement)
