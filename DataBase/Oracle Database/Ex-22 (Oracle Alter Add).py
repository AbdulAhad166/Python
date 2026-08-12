#program for Modifying the Column Sizes of Employee Table
import oracledb as orc
def tablealter():
    try:
        conobj = orc.connect("system/ahad@localhost/free")  # Step-2
        curobj = conobj.cursor()  # Step-3
        # Step-4
        aq="alter table employee add(cname varchar2(10))"
        curobj.execute(aq)
        print("Table Altered Successfully--verify")  # Step-5
    except orc.DatabaseError as err:
        print("Problem in Oracle DB:",err)
#main Program
tablealter()