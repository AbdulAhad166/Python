#Program for adding two lists and calculating salary and bonus using map()
salary=[float(val) for val in input("Enter List of Salaries Separated By Comma: ").split(",")]
bonus=[float(val)for val in input("Enter List of Bonus Separated By Comma: ").split(",")]
if len(salary)>len(bonus):
    for i in range(len(salary)-len(bonus)):
        bonus.append(0)
elif len(salary)<len(bonus):
    for i in range(len(bonus)-len(salary)):
        salary.append(0)
totsal=list(map(lambda x,y:x+y,salary,bonus))
print("----------------------------------")
print("\tSalary\t\tBonus\t\tTotal Salary")
print("-----------------------------------")
for a,b,c in zip(salary,bonus,totsal):
    print("\t{}\t\t{}\t\t{}".format(a,b,c))
print("-----------------------------------")