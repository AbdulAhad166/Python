#Program for Updating The Data Inserted in the Employee Table
import oracledb as orc
def tableupdate():
    try:
        conobj=orc.connect("system/ahad@localhost/free")
        curobj=conobj.cursor()
        uq="update employee set eno=50 where eno=70"
        curobj.execute(uq)
        conobj.commit()
        print("Table Updated---Verify")
    except orc.DatabaseError as error:
        print(error)
tableupdate()