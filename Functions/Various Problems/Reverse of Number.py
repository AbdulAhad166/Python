#Program for accepting any number and get it's Reverse
num=int(input("Enter Any Number: "))
rn=0
tn=num
while num>0:
    d=num%10
    rn=rn*10+d
    num=num//10
else:
    print("\t Reverse ({}) = {}".format(tn,rn))