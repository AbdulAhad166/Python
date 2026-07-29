#StudentMarksReportEx.py
#Validation on student Number--100-200
while(True):
    sno=input("Enter Student Number(100-200):")
    if(sno.isdigit()):
        if(int(sno) in range(100,201)):
            break
        print("\t{} is Invalid Student Number-try".format(sno))
    else:
        print("\t{} is Invalid Student Number-try again".format(sno))
#Validation on student Name
while(True):
    name=input("Enter Student Name:") # GUIDO VAN ROSSUM
    if(name.isspace()):
        print("\tDon't Enter Space for Name-Try Again")
    else:
        words=name.split() # [GUIDO,VAN,ROSUMM]
        if(len(words)==0):
            print("\tU Must Enter    Student Name-try again".format(name))
        else:
            res=True
            for word in words:
                if(not word.isalpha()):
                    res=False
                    break
            if(res):
                name=" ".join(words)
                break
            else:
                print("\t{} is Invalid Student Name-try again".format(name))
#Validation on Marks in C Lang--0-100
while(True):
    cm=input("Enter Marks in C(0-100):")
    if(cm.isdigit()):
        if(int(cm) in range(0,101)):
            break
        print("\t{} is Invalid Student in C Lang-try".format(cm))
    else:
        print("\t{} is Invalid Student in C Lang-try again".format(cm))
#Validation on Marks in CPP Lang--0-100
while(True):
    cppm=input("Enter Marks in CPP(0-100):")
    if(cppm.isdigit()):
        if(int(cppm) in range(0,101)):
            break
        print("\t{} is Invalid Student in CPP Lang-try".format(cppm))
    else:
        print("\t{} is Invalid Student in CPP Lang-try again".format(cppm))
#Validation on Marks in PYTHON Lang--0-100
while(True):
    pym=input("Enter Marks in PYTHON(0-100):")
    if(pym.isdigit()):
        if(int(pym) in range(0,101)):
            break
        print("\t{} is Invalid Student in PYTHON Lang-try".format(pym))
    else:
        print("\t{} is Invalid Student in PYTHON Lang-try again".format(pym))
#Cal totmal marks and percentage
totmarks=int(cm)+int(cppm)+int(pym)
percent=(totmarks/300)*100
#Grade
if(int(cm)<40) or (int(cppm)<40) or (int(pym)<40):
    grade="FAIL"
else:
    if(percent<=100.0 and percent>=75.0):
        grade="DISTINCTION"
    elif(percent<=74.0 and percent>=60.0):
        grade="FIRST"
    elif (percent <= 59.0 and percent >= 50.0):
        grade = "SECOND"
    elif (percent <= 49.0 and percent >= 40.0):
        grade = "THIRD"
print("-"*50)
print("Student Marks Report")
print("-"*50)
print("\tStudent Number:{}".format(sno))
print("\tStudent Name:{}".format(name))
print("\tStudent Marks in C:{}".format(cm))
print("\tStudent Marks in CPP:{}".format(cppm))
print("\tStudent Marks in PYTHON:{}".format(pym))
print("\tStudent Total Marks:{}".format(totmarks))
print("\tStudent Percentage:{}".format(percent))
print("\tStudent Grade:{}".format(grade))
print("-"*50)



