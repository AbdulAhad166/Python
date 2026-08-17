#program for Storing sno,name and marks By using Classes and Objects
class Student:pass


#Main Program
#Create Two Objects of Student Class
s1=Student()
s2=Student()
print("Memory Address of s1 object= ",id(s1))
print("Memory Address of s2 object= ",id(s2))
print("-------------------------------------------------")
#Add Student Details--Instance Data Members to s1 Object--Through an Object
s1.sno=100
s1.name="Rossum"
s1.marks=45.67
#Add Student Details--Instance Data Members to s2 Object--Through an Object
s2.sno=200
s2.name="Travis"
s2.marks=55.17
#Display First Student Object s1 Data
print("---------------------------------------------")
print("First Student Data")
print("---------------------------------------------")
print("\tStudent Number:{}".format(s1.sno))
print("\tStudent Name:{}".format(s1.name))
print("\tStudent Marks:{}".format(s1.marks))
print("---------------------------------------------")
print("Second Student Data")
print("---------------------------------------------")
print("\tStudent Number:{}".format(s2.sno))
print("\tStudent Name:{}".format(s2.name))
print("\tStudent Marks:{}".format(s2.marks))
print("---------------------------------------------")
