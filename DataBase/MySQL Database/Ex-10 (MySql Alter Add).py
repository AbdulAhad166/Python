#Program for Altering---Add in Employee Table
import mysql.connector as sq
def recordadd():
        try:
            conobj=sq.connect(host="localhost",user="root",password="ahad",use_pure=True,database="batch6pm")
            cur=conobj.cursor()
            aq="alter table employee add(cname varchar(20) not null)"
            cur.execute(aq)
            conobj.commit()
            print("Table Altered Successfully---Verify")
        except sq.DatabaseError as db:
            print("Problem in MySql Database",db)
#Main Program
recordadd()