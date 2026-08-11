#Program for Reading the Records from Table Along With Column Names
import oracledb as orc
def selectrecords():
    try:
        conobj=orc.connect("system/ahad@localhost/free")
        curobj=conobj.cursor()
        #Get Records from employee
        sq="select * from employee order by sal asc"
        curobj.execute(sq)
        #Get Column Names
        for colinfo in curobj.description:
            print("\t {}".format(colinfo[0]),end="\t")
        print()
        #Get The Records
        records=curobj.fetchall()
        if len(records)==0:
            print("No Records Found")
        else:
            for record in records:
                for val in record:
                    print("\t {}".format(val),end="\t")
                print()
            print("-----------------------------------")
    except orc.DatabaseError as db:
        print("Problem in Oracle Database",db)
#Main Program
selectrecords()
