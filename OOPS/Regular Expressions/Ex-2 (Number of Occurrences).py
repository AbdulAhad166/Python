#Program For Finding Number of Occurrences That are Present and count of the words
import re
gd="Python is an oop lang.Python is also Functional Programming Language"
sp="Python"
matres=re.search(sp,gd)  #Here matres is an object of <class,re.match> OR <class,NoneType>
if matres!=None:
    print("Search Successful")
    print("\t Start Index: ",matres.start())
    print("\t End Index: ",matres.end())
    print("\t Matched Value: ",matres.group())
else:
    print("Search Un-Successful")