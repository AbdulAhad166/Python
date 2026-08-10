#program for Removing the Table from Oracle Database
import oracledb as orc
def tabledrop():
    try:
        conobj=orc.connect("system/ahad@localhost/free")
        curobj=conobj.cursor()
        dq="drop table student"
        curobj.execute(dq)
        print("table Dropped Successfully---Verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle Database",db)
#Main Program
tabledrop()