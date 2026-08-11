#Program for Reading the Records from employee --- fetchone()
import oracledb as orc
def recordselect():
    try:
        conobj=orc.connect("system/ahad@localhost/free")
        curobj=conobj.cursor()
        #Get The Records from employee
        sq="select * from employee"
        curobj.execute(sq)
        #Get Records from curobj
        while True:
            record=curobj.fetchone()
            if record is not None:
                for val in record:
                    print("\t {}".format(val),end="\t")
            else:
                break
    except orc.DatabaseError as db:
        print("Problem in Oracle Database",db)
#Main Program
recordselect()