#Program for Cal simple interest with all data validations
p=float(input("Enter the principle Amount: " ))
t=float(input("Enter time: "))
r=float(input("Enter the Rate of Interest:"))
if(p>0) and (t>0) and (r>0):
    si=p*t*r
    print("\t Principle Amount: {}".format(p))
    print("\t Time: {}".format(t))
    print("\t Rate of Interest: {}".format(r))
    print("\t Simple Interest: {}".format(si))
if(p<0):
    print("\t Invalid Principle Amount: {}".format(p))
if(t<0):
    print("\t Invalid Time: {}".format(t))
if(r<0):
    print("\t Invalid Rate of Interest: {}".format(r))
