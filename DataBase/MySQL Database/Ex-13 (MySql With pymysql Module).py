#Program for Reading the Records from Table along with Column names
import pymysql as sq
def selectrecords():
    try:
        conobj=sq.connect(host="localhost",user="root",password="ahad",database="batch6pm")
        curobj=conobj.cursor()
        #Get The Records From Employee Table
        rq="select * from employee order by eno"
        curobj.execute(rq)
        #Get Column Names
        for colinfo in curobj.description:
            print("\t {}".format(colinfo[0]),end="\t")
        print()
        #Get The Records
        records=curobj.fetchall()
        if len(records)==0:
            print("\t No Records Found")
        else:
            for record in records:
                for val in record:
                    print("\t {}".format(val),end="\t")
                print()
    except sq.DatabaseError as db:
        print("Problem in MySql Database",db)
#Main Program
selectrecords()
