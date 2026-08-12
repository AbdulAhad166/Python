#Program For Reading Records from employee---fetchall()
import mysql.connector as sq
def recordselect():
    try:
        conobj=sq.connect(host="localhost",user="root",password="ahad",use_pure=True,database="batch6pm")
        curobj=conobj.cursor()
        #Get Records From employee table
        rq="select * from employee"
        curobj.execute(rq)
        #Get The Records from the curobj
        records=curobj.fetchall()
        for record in records:
            for val in record:
                print("\t {}".format(val),end="\t")
            print()
    except sq.DatabaseError as db:
        print("Problem in MySql Database",db)
#Main Program
recordselect()