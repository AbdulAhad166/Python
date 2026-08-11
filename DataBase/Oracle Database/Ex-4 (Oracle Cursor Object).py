#Program for Creating Cursor Object
import oracledb as orc. #step-1
conobj=orc.connect("system/ahad@localhost/free")
print("Python Program Got Connection From Oracledb")
print("type of conobj= ",type(conobj))
curobj=conobj.cursor()
print("Python Program Created Cursor Object")
print("Type of curobj= ",type(curobj))