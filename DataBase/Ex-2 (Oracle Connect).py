#Program for Demonstrating How To Get Connection from oracledb
import oracledb as orc
try:
    conobj=orc.connect("system/ahad@127.0.0.1/free")
    print("Python Program Got Connection from oracledb")
    print("Type of conobj= ",type(conobj))
except orc.DatabaseError as db:
    print("Problem in Oracle DataBase: ",db)