#Program for Creating a CSV File By Using writer()---List in List
import csv
hnames=["SNO","SNAME","MARKS"]
records=[[100,"Guido",70.00],
         [200,"Travis",80.00],
         [300,"Ford",90.00],
         [400,"Dennis",95.00],
         [500,"Honda",95.00]]
#Choose CSV File and Open in write Mode
with open("stud.csv","w",newline="") as fp:
    csvwr=csv.writer(fp)
    #Write the Header Names
    csvwr.writerow(hnames)
    #Write the Records
    csvwr.writerows(records)
    print("CSV File Created---Verify")