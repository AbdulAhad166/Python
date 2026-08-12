#Program for Removing the Database from MySql
import mysql.connector as mc #Step-1
def removedb():
    try:
        conobj=mc.connect(host="127.0.0.1",
                          user="root",
                           passwd="ahad" ,
                          use_pure=True) #Step-2
        cur=conobj.cursor()#Step-3
        #Step-4
        dc="drop database employee"
        cur.execute(dc)
        print("Data Base Removed in MySQL--verify")
    except mc.DatabaseError as db:
        print("Problem in MySQL Database:",db)
#Main Program
removedb() # Function Call