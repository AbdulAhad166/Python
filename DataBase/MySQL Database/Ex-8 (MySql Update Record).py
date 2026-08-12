# Program for Updating Emp Sal, Emp Comp Name of Employee table
import mysql.connector as sq
def recordupdate():
    while True:
        try:
            conobj = sq.connect(
                host="127.0.0.1",
                user="root",
                password="ahad",
                use_pure=True,
                database="batch6pm"
            )
            curobj = conobj.cursor()
            # Accept Employee Number for Updating Salary and Company Name
            empno = int(input("Enter Employee Number: "))
            newsal = float(input("Enter New Salary: "))
            newcname = input("Enter New Company Name: ")
            uq = "UPDATE employee SET sal=%s, cname=%s WHERE eno=%s"
            curobj.execute(uq, (newsal, newcname, empno))
            conobj.commit()
            if curobj.rowcount > 0:
                print("Record Updated---Verify")
            else:
                print("Record Does Not Exist")
            ch = input("Do You Want To Update Another Record? (yes/no): ")
            if ch.lower() == "no":
                print("---------------------------------")
                break
        except sq.DatabaseError as db:
            print("Problem in MySql Database", db)
# Main Program
recordupdate()