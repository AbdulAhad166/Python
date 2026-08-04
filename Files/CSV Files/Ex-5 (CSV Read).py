#Program for CSV File Data Using csv.reader()
import csv
with open("emp.csv",'r') as fp:
    csvr=csv.reader(fp)
    for val in csvr:
        print(val)
    print()
    