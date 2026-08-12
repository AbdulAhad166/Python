#Program for Creating the Database
import mysql.connector as sq
def createdb():
    try:
        conobj=sq.connect(host="localhost",user="root",password="ahad",use_pure=True)
        curobj=conobj.cursor()
        dc="create database batch6pm"
        curobj.execute(dc)
        print("Database Created in MySQL---Verify")
    except sq.DatabaseError as db:
        print("Problem in MySql Database",db)
#Main Program
createdb()