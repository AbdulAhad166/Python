#Program for Creating Cursor Object
import mysql.connector as mc #Step-1
try:
    conobj=mc.connect(host="127.0.0.1",
                      user="root",
                       passwd="ahad" ,
                      use_pure=True) #Step-2
    print("Python Program Got Connection from MySQL")
    cur=conobj.cursor()
    print("Python Program Created in  MySQL")
except mc.DatabaseError as db:
    print("Problem in MySQL:",db)

