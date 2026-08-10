#program for Deleting the Record Based on Employee Number
import oracledb as orc
def recorddelete():
    try:
        conobj=orc.connect("system/ahad@localhost/free")
        curobj=conobj.cursor()
        dq="delete from employee where eno=11"
        curobj.execute(dq)
        conobj.commit()
        if curobj.rowcount>0:
            print("{} Record Deleted Successfully".format(curobj.rowcount))
        else:
            print("Record Does Not Exist")
    except orc.DatabaseError as db:
        print("Problem in Oracle Database",db)
#Main Program
recorddelete()