#Program for Creating a Table Employee
import oracledb as orc
def tablecreate():
    try:
        conobj=orc.connect("system/ahad@localhost/FREE")
        curobj=conobj.cursor()
        tc="Create table employee(eno number(3) primary key,name varchar2(10) not null,sal number(5,2) not null)"
        curobj.execute(tc)
        conobj.commit()
        print("Table Created Successfully---Verify")
    except orc.DatabaseError as er:
        print("Problem in Oracle Database",er)
#Main Program
tablecreate()
