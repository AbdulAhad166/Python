#Program for Storing sno,name and marks By using Classes and Objects
class Student:pass


#Main Program
#Create Two Objects of Student Class
s1=Student()
s2=Student()
print("Content of First Object s1= ",s1.__dict__)
print("Number of Values in s1= ",len(s1.__dict__))
print("-"*50)
print("Content of Second Object s1= ",s2.__dict__)
print("Number of Values in s2= ",len(s2.__dict__))
#Add Student Details--Instance Data Members to s1 object--Through an object
s1.sno=100
s1.name="Rossum"
s1.marks=45.67
#Add Student Details--Instance Data Members to s2 Object--Through an Object
s2.sno=200
s2.name="Travis"
s2.marks=55.17
#Display First Student Object s1 Data
print("-"*50)
print("First Student Data")
print("-"*50)
print("\t Number of Values in s1= ",len(s1.__dict__))
for id,ib in s1.__dict__.items():
    print("\t {}--->{}".format(id,ib))
print("-"*50)
print("Second Student Data")
print("-"*50)
for id,ib in s2.__dict__.items():
    print("\t {}--->{}".format(id,ib))
print("-"*50)