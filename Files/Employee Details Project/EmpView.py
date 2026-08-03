#EmpView.py<---Module Name
import pickle
def ViewSingleEmployee():
    records=[]
    with open("Empproject.data","rb") as fp:
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    empno=int(input("Enter Employee Number: "))
    found=False
    for record in records:
        if record[0]==empno:
            rec=record
            found=True
            break
    if found:
        print("\t Employee Number: {}".format(rec[0]))
        print("\t Employee Name: {}".format(rec[1]))
        print("\t Employee Salary: {}".format(rec[2]))
    else:
        print("\t Employee Does Not Exist")
def ViewAllEmployees():
    with open("Empproject.data","rb") as fp:
        print("\tEmpNo\t\tEmpName\t\tEmpSalary")
        while True:
            try:
                record=pickle.load(fp)
                for val in record:
                    print("\t {}".format(val),end="\t")
                print()
            except EOFError:
                break
