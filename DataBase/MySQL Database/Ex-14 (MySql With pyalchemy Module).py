#MySQLOpWithSQLAlchmeyMod.py
from sqlalchemy import create_engine, text
engine = create_engine("mysql+pymysql://root:ahad@localhost/batch6pm")
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM employee"))
    print("---------------------------------------------")
    for row in result:
        for val in row:
            print("\t{}".format(val),end="\t")
        print()
    print("---------------------------------------------")