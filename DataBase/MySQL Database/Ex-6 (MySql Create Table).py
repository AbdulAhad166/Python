#Program For Creating a Table
import mysql.connector as sq
def tablecreate():
    try:
        conobj=sq.connect(host="localhost",user="root",password="ahad",use_pure=True,database="batch6pm")
        cur=conobj.cursor()
        tc="create table employee(eno int primary key,name varchar(30) not null,sal real,cname varchar(10) not null)"
        cur.execute(tc)
        conobj.commit()
        print("Table Created Successfully---Verify")
    except sq.DatabaseError as db:
        print("Problem in MySql Database",db)
#Main Program
tablecreate()