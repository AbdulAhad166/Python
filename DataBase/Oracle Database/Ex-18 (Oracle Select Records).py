#Program for Reading The Records from employee --- fetchall()
import oracledb as orc
def recordselect():
    try:
        conobj=orc.connect("system/ahad@localhost/free")
        curobj=conobj.cursor()
        #Get Records from employee
        sq="select * from employee order by eno"
        curobj.execute(sq)
        #Get Records from cursor object
        records=curobj.fetchall()
        for record in records:
            for val in record:
                print("\t {}".format(val),end="\t")
            print()
        print("----------------------------------------")
    except orc.DatabaseError as e:
        print("Problem in Oracle Database",e)
#Main Program
recordselect()