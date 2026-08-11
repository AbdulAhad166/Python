#Program For Reading The Records From Employee---fetchmany()
import oracledb as orc
def tableinsert():
    try:
        conobj=orc.connect("system/ahad@localhost/free")
        curobj=conobj.cursor()
        #Get The Records From employee Table
        sq="select * from employee order by eno asc"
        curobj.execute(sq)
        records=curobj.fetchmany(3)
        for record in records:
            for val in record:
                print("\t {}".format(val),end="\t")
            print()
        print("------------------------------------------")
    except orc.DatabaseError as e:
        print("Problem in Oracle Database",e)
#Main Program
tableinsert()