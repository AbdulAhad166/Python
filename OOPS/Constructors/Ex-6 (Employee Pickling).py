#Main File
import pickle
from Employee import Employee
class EmployeePick:
    def getempdata(self):
        self.eno=int(input("Enter Employee Number: "))
        self.name=input("Enter Employee Name: ")
        self.sal=float(input("Enter Employee Salary: "))
    def saveempdata(self):
        with open("emp.pick","ab") as fp:
            eo=Employee(self.eno,self.name,self.sal)
            pickle.dump(eo,fp)
            print("Employee Record Saved---Verify")
#Main Program
epo=EmployeePick()
epo.getempdata()
epo.saveempdata()