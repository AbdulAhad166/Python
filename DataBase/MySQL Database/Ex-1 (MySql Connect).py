#Program Fro Connecting
import mysql.connector as sq
try:
    conobj = sq.connect(
        host="localhost",
        user="root",
        password="ahad"
    )
    print("Connected successfully")
except Exception as e:
    print("Problem in MySQL Database", e)