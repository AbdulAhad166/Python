#Program for Demonstrating the Need of  Keyword Variable Length Arguments
def findTotalMarks(sno,sname,cls,*intmarks,city="HYD",**submarks):
    print("-"*50)
    print("\tStudent Number: {}".format(sno))
    print("\tStudent Name: {}".format(sname))
    print("\tStudent Class Name: {}".format(cls))
    print("\tInternal Marks: {}".format(intmarks))
    print("-"*50)
    print("\tSubject\tMarks")
    print("-"*50)
    tot=0
    for subject,marks in submarks.items():
        print("\t{}\t{}".format(subject,marks))
        tot=tot+marks
    print("\tTotal :{}".format(tot))
#Main Program
findTotalMarks(100,"Yamal","X",10,20,15,24,13,12,Telugu=80,English=88,Hindi=70,Maths=90,Science=80,Social=90)
findTotalMarks(101,"Hurricane","XII",14,15,18,13,17,English=80,Sanskrit=99,Maths=75,Physics=58, Chemistry=55)
findTotalMarks(102,"Ronaldo","B.Tech",OS=50,DBMS=60,NW=50)
findTotalMarks(103,"BB","Politics",Eco=11,PolSc=10,city="USA")
findTotalMarks(103,"RS","Politics",10,12,city="RSA",Eco=66,PolSc=80)