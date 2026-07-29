#program for accepting the age of the Person and decide
#whether Eligible to Vote OR Not
while(True):
    age=int(input("Enter Age of Voter: "))
    if age<=0:
        print("Invalid Input")
    if (age>=18):
        print("\t{} Years Citizen is Eligible To Vote".format(age))
        break
    else:
        print("\t{} Years Citizen is Not Eligible To Vote".format(age))
