#Program for Reading the CSV File Data Using csv.DictReader()
import csv
with open("emp.csv","r") as fp:
    csvdr=csv.DictReader(fp)  #Here csvdr is an object of <class, csv.DictReader>
    for record in csvdr:  #Here record is of type <class,dict>
        for hn,hv in record.items():
            print("\t {}--->{}".format(hn,hv))
