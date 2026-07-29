#icici.py<---File Name acts as Module Name
bname="ICICI"
addr="HYDERABAD"    #Here bname,addr are Global Variables
def simpleint():
    P=float(input("Enter Principle Amount: "))
    T=float(input("Enter Time: "))
    R=float(input("Enter Rate of Interest:"))
    #Calculate si and totalamount
    si=(P*T*R)/100
    totamt=P+si
    print("--------------------------------------")
    print("\t Results of Simple Interest")
    print("--------------------------------------")
    print("\t\t Principle Amount: ",P)
    print("\t\t Time: ",T)
    print("\t\t Rate of Interest: ",R)
    print("\t\t Simple Interest: ",si)
    print("\t\t Total Amount: ",totamt)
    print("--------------------------------------")