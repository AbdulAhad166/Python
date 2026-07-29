#Program for Calculate simple interest with all data validations
p=float(input("Enter Principle Value: "))
t=float(input("Enter Time: "))
r=float(input("Enter Rate of Interest: "))
if (p>0 and t>0 and r>0):
    si=p*t*r
    print("Result of Simple Interest")
    print("\t Principle Amount:",p)
    print("\t Time:",t)
    print("\t Rate of Interest:",r)
    print("\t Simple Interest:",si)
else:
    if (p<=0):
        print("\t Invalid Principle Amount",p)
    if (t<=0):
        print("\t Invalid Time",t)
    if (r<=0):
        print("\t Invalid Rate of Interest",r)

