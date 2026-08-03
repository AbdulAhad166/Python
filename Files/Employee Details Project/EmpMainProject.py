#EmpMainProject.py<---Main Program
from EmpMenu import menu
from EmpAdd import addEmp
from EmpView import ViewSingleEmployee,ViewAllEmployees
from EmpSearch import searchEmployee
from EmpUpdate import updateEmployee
from EmpDelete import deleteEmployee
while True:
    try:
        menu()
        ch=int(input("Enter Your Choice: "))
        match ch:
            case 1:
                addEmp()
            case 2:
                deleteEmployee()
            case 3:
                updateEmployee()
            case 4:
                ViewSingleEmployee()
            case 5:
                ViewAllEmployees()
            case 6:
                searchEmployee()
            case 7:
                exit()
    except ValueError:
        print("\t Do Not Enter Alnums,Str,Symbols---Try Again")





