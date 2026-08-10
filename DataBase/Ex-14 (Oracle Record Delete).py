#program for Deleting the Record Based on Employee Number
import oracledb as orc
def recorddelete():
    while True:
        try:
            conobj=orc.connect("system/ahad@localhost/free")
            curobj=conobj.cursor()
            eno=int(input("Enter Employee Number To Delete: "))
            dq="delete from employee where eno=%d"
            curobj.execute(dq % eno)
            conobj.commit()
            if curobj.rowcount>0:
                print("{} Record Deleted Successfully".format(curobj.rowcount))
            else:
                print("Record Does Not Exist")
            ch=input("Do You Want To Delete Another Record? (yes/no): ")
            if ch.lower()=="no":
                print("---------------------------------")
                break
        except orc.DatabaseError as db:
            print("Problem in Oracle Database",db)
#Main Program
recorddelete()