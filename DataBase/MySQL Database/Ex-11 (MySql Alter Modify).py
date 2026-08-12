#program for Modifying the Column Sizes of Employee Table
import mysql.connector as sq
def tablealter():
    try:
        conobj=sq.connect(host="localhost",user="root",password="ahad",use_pure=True,database="batch6pm")
        curobj=conobj.cursor()
        aq="alter table employee modify eno int, modify name varchar(20)"
        curobj.execute(aq)
        conobj.commit()
        print("Table Altered Successfully---Verify")
    except sq.DatabaseError as db:
        print("Problem in MySql Database",db)
#Main Program
tablealter()

