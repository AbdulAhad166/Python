#Program for Updating Emp Sal, Emp Comp Name of Employee table
import oracledb as orc
def tableupdate():
    try:
        conobj=orc.connect("system/ahad@localhost/free")
        curobj=conobj.cursor()
        #Accept The Employee Details
        eno=int(input("Enter Employee Number: "))
        newsal=float(input("Enter Employee New Salary: "))
        uq="update employee set sal=%f where eno=%d"%(newsal,eno)
        curobj.execute(uq)
        conobj.commit()
        if curobj.rowcount>0:
            print("{} Record Updated Successfully".format(curobj.rowcount))
        else:
            print("Record Does Not Exist")
    except orc.DatabaseError as db:
        print("Problem in Oracle Database",db)
#Main Program
tableupdate()