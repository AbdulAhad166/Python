#program for accepting Employee Details from KBD and Insert as Record in Employee Table
import oracledb as orc
def tableinsert():
    while True:
        try:
            conobj=orc.connect("system/ahad@localhost/free")
            curobj=conobj.cursor()
            #Accept the Employee Details
            eno=int(input("Enter Employee Number: "))
            name=input("Enter Employee Name: ")
            sal=float(input("Enter Employee Salary: "))
            iq="insert into employee values('%d','%s','%f')"%(eno,name,sal)
            curobj.execute(iq)
            conobj.commit()
            print("{} Record Inserted Successfully".format(curobj.rowcount))
            ch=input("Do You Want To Insert Another Record? (yes/no): ")
            if ch.lower()=="no":
                print("------------------------")
                break
        except orc.DatabaseError as db:
            print("Problem in Oracle Database",db)
#Main Program
tableinsert()
