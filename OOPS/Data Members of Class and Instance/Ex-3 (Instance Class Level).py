#Program for Storing sno,name,marks along with Common Values by using classes and objects
class Student:
    crs="PYTHON"
    city="HYDERABAD"  #Here crs,city are Class Level Data Members
#Main Program
#Create Two objects
s1=Student()
s2=Student()
#Add Student Details -- Instance Data Members to s1 object --Through an object
s1.sno=100
s1.name="Rossum"
s1.marks=50.00
#Add Student Details -- Instance Data Members to s2 object --Through an object
s2.sno=200
s2.name="Travis"
s2.marks=60.00
#Display First Student Object s1 Data
print("-"*50)
print("First Student Data")
print("-"*50)
print("\t Number of Values Present in First Student Data= ",len(s1.__dict__))
print("\t Student Number= {}".format(s1.sno))
print("\t Student Name= {}".format(s1.name))
print("\t Student Marks= {}".format(s1.marks))
print("\t Student Course= {}".format(Student.crs))
print("\t Student City= {}".format(Student.city))
print("-"*50)
print("Second Student Data")
print("-"*50)
print("\t Number of Values Present in Second Student Data= ",len(s2.__dict__))
print("\t Student Number= {}".format(s2.sno))
print("\t Student Name= {}".format(s2.name))
print("\t Student Marks= {}".format(s2.marks))
print("\t Student Course= {}".format(Student.crs))
print("\t Student City= {}".format(Student.city))

