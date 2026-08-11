#Program for Inserting The Values in the Table Employee
import oracledb as orc
def tableinsert():
    try:
        conobj=orc.connect("system/ahad@localhost/free")
        curobj=conobj.cursor()
        curobj.execute("insert into employee values(20,'Travis',4.5)")
        curobj.execute("insert into employee values(30,'Dennis',5.5)")
        curobj.execute("insert into employee values(40,'Nobita',6.5)")
        conobj.commit()
        print("Record Inserted Successfully---Verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle Database",db)

#Main Program
tableinsert()