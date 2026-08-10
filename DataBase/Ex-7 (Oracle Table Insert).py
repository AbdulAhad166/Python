#Program for Accepting Employee Details Dynamically and Insert as Records in Employee Table
import oracledb as orc
def tableinsert():
    try:
        conobj=orc.connect("system/ahad@localhost/free")
        curobj=conobj.cursor()
        #Accept Employee Details
        empno=int(input("Enter Employee Number: "))
        name=input("Enter Employee Name: ")
        sal=float(input("Enter Employee Salary: "))
        iq="insert into employee values('%d','%s','%f')"%(empno,name,sal)
        curobj.execute(iq)
        conobj.commit()
        print("{} Record Inserted Successfully".format(curobj.rowcount))
    except orc.DatabaseError as error:
        print("Problem in Database",error)
#Main Program
tableinsert()