#Program for Reading All the Column Names with Meta Data
import oracledb as orc
def selectcolumn():
    try:
        conobj=orc.connect("system/ahad@localhost/free")
        curobj=conobj.cursor()
        #Get Records of employee
        sq="select * from employee"
        curobj.execute(sq)
        #Get Records from curobj
        for colinfo in curobj.description:
            print("\t {}".format(colinfo[0]),end="\t")
        print()
    except orc.DatabaseError as err:
        print("Problem in Oracle Database",err)
#Main Program
selectcolumn()