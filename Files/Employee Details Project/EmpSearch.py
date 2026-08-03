#EmpSearch.py<---Module Name
import pickle
def searchEmployee():
    records=[]
    with open("Empproject.data","rb") as fp:
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    empno=int(input("Enter Employee Number To Search: "))
    found=False
    for record in records:
        if record[0]==empno:
            found=True
            break
    if found:
        print("Employee Valid")
    else:
        print("Employee Not Valid")
