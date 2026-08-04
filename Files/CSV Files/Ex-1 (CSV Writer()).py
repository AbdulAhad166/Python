#Program for Creating a CSV File Using writer()---List in List
import csv #Step-1
hnames=["ENO", "ENAME", "SAL"]   #Step-2
records=[[100,"Rossum",4.5],
         [200,"Travis",5.5],
         [300,"Dennis",6.5],
         [400,"Nobita",7.5],
         [500,"Sunio",8.5]]
#Choose the CSV File and Open in the Write Mode
with open("emp.csv","w",newline="") as fp:    #Step-4
    csvwr=csv.writer(fp)  #Step-5---Here csvwr is an object of <class,csv.writer>
    #Write the Header Names
    csvwr.writerow(hnames) #Step-6
    #Write the Records
    csvwr.writerows(records)   #Step-7
    print("CSV File Created---Verify")