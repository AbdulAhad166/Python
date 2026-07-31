#Program for Saving Student Data into File
with open("stud1.data", "a") as fp:
    fp.write(str(100)+"\t")
    fp.write("Guido"+"\t")
    fp.write(str(88.88)+"\n")
    print("Student Data Saved In File---Verify")