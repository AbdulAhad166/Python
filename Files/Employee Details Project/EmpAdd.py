#EmpAdd.py<---Module Name
import pickle
def addEmp():
    with open("Empproject.data","ab") as fp:
        empno=int(input("Enter Employee Number: "))
        empname=input("Enter Employee Name: ")
        empsal=float(input("Enter Employee Salary: "))
        #Iterable Object
        lst=list()
        lst.append(empno)
        lst.append(empname)
        lst.append(empsal)
        #Save the Iterable Object Data into File
        pickle.dump(lst,fp)
        print("Employee Details Saved---Verify")


