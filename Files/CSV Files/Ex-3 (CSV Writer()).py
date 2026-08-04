#Program For Creating a CSV File By Using DictWriter()---dict in list
import csv
hnames=["PID","PNAME","PRICE"]
records=[{"PID":1,"PNAME":"KitKat","PRICE":20.00},
         {"PID":2,"PNAME":"5 Star","PRICE":10.00},
         {"PID":3,"PNAME":"Dairy Milk","PRICE":60.00},
         {"PID":4,"PNAME":"Snickers","PRICE":50.00},
         {"PID":5,"PNAME":"Gems","PRICE":10.00}]
with open("products.csv","w") as fp:
    csvdwr=csv.DictWriter(fp,fieldnames=hnames) #Here csvwdr is an object of <class,csv.DictWriter>
    #csvdwr obejct contains TWO Functions: 1. writeheader()  2.writerows()
    csvdwr.writeheader()   #Will write / save Header names as Columns in CSV File
    #Write / Save Records in CSV File
    csvdwr.writerows(records)
    print("CSV File Created---Verify")

