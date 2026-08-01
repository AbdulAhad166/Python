#Program For Reading Employee Details From Key Board and Save Them As Records in file
#of secondary memory by using Pickling Concept
def saverecord():
    import pickle
    with open("emp.pick", "ab") as fp:
        while True:
            empno=int(input("Enter Employee Number: "))
            empname=input("Enter Employee Name: ")
            empsal=float(input("Enter Employee Salary: "))
            # Create an empty list-Iterable Object
            lst=list()
            lst.append(empno)
            lst.append(empname)
            lst.append(empsal)
            #Save the Iterable Object Data Into A File
            pickle.dump(lst,fp)
            print("Employee Records Saved In File")
            ch=input("Do You Want To Insert Another Record (Yes/No): ")
            if ch.title()=="No":
                break
#Main Program
saverecord()
