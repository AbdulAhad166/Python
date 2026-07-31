#Program For Saving Iterable Object Data Into The File
with open("stud.data","a") as fp:
    #Take an Iterable Object
    itrobj={1:"PYTHON",2:"JAVA",3:"C",4:"C++",5:"C#"}
    #Now Save The Iterable Objects Into The File
    fp.writelines(str(itrobj)+"\n")
    print("\t Iterable Object Data Saved In File---Verify")