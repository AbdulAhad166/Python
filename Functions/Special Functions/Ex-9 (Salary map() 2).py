#Program for calculating salary with adding bonus into a list using map()
print("Enter List of Values Separated By Comma: ")
oldsal=[float(val) for val in input().split(",")]
newsal=list(map(lambda sal:sal+sal*50/100,oldsal))
print("--------------------------------")
print("\tOld Salary\t\tNew Salary")
print("--------------------------------")
for old,new in zip(oldsal,newsal):
    print("\t{}\t\t{}".format(old,new))
print("--------------------------------")