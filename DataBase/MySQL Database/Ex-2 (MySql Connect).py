#Program for Connecting to Mysql Database
import mysql.connector as sq
try:
    conobj=sq.connect(host="127.0.0.1",user="root",passwd="ahad",use_pure=True)
    print("Python Got Connection From MySql Database")
except sq.DatabaseError as db:
    print("Problem in MySql Database")