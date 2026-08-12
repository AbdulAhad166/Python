#Program For Deleting the Records from employee table
import mysql.connector as sq
def deleterecord():
    while True:
        try:
            conobj=sq.connect(host="localhost",user="root",password="ahad",use_pure=True,database="batch6pm")
            curobj=conobj.cursor()
            #Accpet Empno to Delete the Record
            eno=int(input("Enter Employee Number To Delete: "))
            dq="delete from employee where eno=%d"
            curobj.execute(dq % eno)
            conobj.commit()
            if curobj.rowcount>0:
                print("\t {} Record Deleted Successfully".format(curobj.rowcount))
            else:
                print("Record Does Not Exist")
            ch=input("Do You Want To Delete Another Record? (yes/no): ")
            if ch.lower()=="no":
                print("-----------------------------------------------")
                break
        except sq.DatabaseError as db:
            print("Problem in MySql Database",db)
        except ValueError:
            print("Do Not Enter Alnums,Str,Symbols---Try Again")
#Main Program
deleterecord()