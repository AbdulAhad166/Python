# Program for Database Connectivity with Inserting Values Using Constructor Method
import mysql.connector as sq
class Employee:
    def __init__(self):
        self.eno = int(input("Enter Employee Number: "))
        self.name = input("Enter Employee Name: ")
        self.sal = float(input("Enter Employee Salary: "))
        self.cname = input("Enter Company Name: ")
    def savedata(self):
        try:
            con = sq.connect(host="127.0.0.1",
                             user="root",
                             password="ahad",
                             use_pure=True,
                             database="batch6pm")
            curobj = con.cursor()
            iq = "insert into employee values(%d,'%s',%f,'%s')" % (
                self.eno, self.name, self.sal, self.cname)
            curobj.execute(iq)
            print("\t{} Record Inserted Successfully".format(curobj.rowcount))
            con.commit()
        except sq.DatabaseError as db:
            print("Problem in MySQL DB:", db)
# Main Program
s = Employee()
s.savedata()