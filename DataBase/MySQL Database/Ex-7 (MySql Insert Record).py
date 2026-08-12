#Program for Inserting the Records in Employee Table
import mysql.connector as sq
def recordinsert():
    while True:
        try:
            conobj=sq.connect(host="localhost",user="root",password="ahad",use_pure=True,database="batch6pm")
            cur=conobj.cursor()
            #Accept Employee Details
            empno=int(input("Enter Employee Number: "))
            name=input("Enter Employee Name: ")
            sal=float(input("Enter Employee Salary: "))
            cname=input("Enter Employee Company Name: ")
            iq="insert into employee values(%d,'%s',%f,'%s')"%(empno,name,sal,cname)
            cur.execute(iq)
            conobj.commit()
            print("\t {} Records Inserted Successfully".format(cur.rowcount))
            ch=input("Do You Want To Insert More Records? (yes/no): ")
            if ch.lower()=="no":
                print("-------------------------------------------------")
                break
        except sq.DatabaseError as db:
            print("Problem in MySql Database",db)
#Main Program
recordinsert()
