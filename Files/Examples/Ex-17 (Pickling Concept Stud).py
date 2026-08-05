#Program For Reading Student Details From Key Board and Save Them As Records in file
#of secondary memory by using Pickling Concept
def saverecord():
    import pickle
    with open("stud.pick","ab") as fp:
        while True:
            studno=int(input("Enter Student Number: "))
            studname=input("Enter Student Name: ")
            studmarks=float(input("Enter Student Marks: "))
            #Create an empty list-Iterable Object
            lst=list()
            lst.append(studno)
            lst.append(studname)
            lst.append(studmarks)
            #Save the Iterable Object Data into the File
            pickle.dump(lst,fp)
            print("Student Records Saved in File")
            ch=input("Do You Want To Insert Another Record? (Yes/No): ")
            if ch.title()=="No":
                break
#Main Program
saverecord()