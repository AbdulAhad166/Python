#Program for accepting a List of Values and Get Its Reverse
#without using extended Slicing and reverse()
def readvals():
    n=int(input("Enter How Many Numbers You Want: "))
    if n<=0:
        return []
    else:
        lst=[]
        for i in range(1,n+1):
            val=float(input("Enter {} Value: ".format(i)))
            lst.append(val)
        return lst
def reverse():
    vals=readvals()
    if len(vals)==0:
        print("\t List is Empty")
    else:
        print("\tOriginal list=",vals)
        left=0
        right=len(vals)-1
        while left<right:
            vals[left],vals[right]=vals[right],vals[left]
            left=left+1
            right=right-1
        else:
            print("Reverse List=",vals)
#Main Program
reverse()
