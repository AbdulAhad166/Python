#Program for calculating the salary and bonus using map()
def hike(sal):
    return sal+sal*50/100
#Main Program
oldsal=[100,200,300,400,500,600]
m=map(hike,oldsal)  #Here  m is an object of <class,map>
#Convert map object into list
hs=list(m)
print("----------------------------")
print("\tOld Salary\t\tNew Salary")
print("----------------------------")
for old,new in zip(oldsal,hs):
    print("\t{}\t\t{}".format(old,new))
print("----------------------------")
