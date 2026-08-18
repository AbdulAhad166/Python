#Program for Database Connectivity with Inserting Values Using Constructor Method
import mysql.connector as sq
class Employee:
    def __init__(self):
        try:
            self.con=sq.connect(host="localhost",user="root",password="ahad",use_pure=True,database="batch6pm")
            self.curobj=self.con.cursor()
            #Accept the Employee Details
            self.sno=int(input("Enter Employee Number: "))
            self.name=input("Enter Employee Name: ")
            self.sal=float(input("Enter Employee Salary: "))
            self.cname=input("Enter Company Name: ")
        except sq.DatabaseError as db:
            print("Problem in MYSQL Database",db)
    def recordinsert(self):
        try:
            iq="insert into employee values(%d,'%s',%f,'%s')"%(self.sno,self.name,self.sal,self.cname)
            self.curobj.execute(iq)
            self.con.commit()
            print("\t {} Record Inserted Successfully".format(self.curobj.rowcount))
        except sq.DatabaseError as db:
            print("Problem in MYSQL Database",db)
#Main Program
eo=Employee()
eo.recordinsert()
