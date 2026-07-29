#Program for adding two lists contents using map()
salary=[1000,2000,3000,4000,5000]
bonus=[500,600,700,800,900]
totsal=list(map(lambda x,y:x+y,salary,bonus))
print("--------------------------")
print("\tSalary\t\tBonus\t\tTotal Salary")
print("--------------------------")
for a,b,c in zip(salary,bonus,totsal):
    print("\t{}\t\t{}\t\t{}".format(a,b,c))