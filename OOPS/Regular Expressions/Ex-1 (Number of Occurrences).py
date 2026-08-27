#Program For Finding Number of Occurrences of Any Word in Given Sentence
import re
gd="Python is an oop lang.Python is also Functional Programming Language"
sp="Python"
matres=re.findall(sp,gd)  #Here matres is an object of <class,list>
if len(matres)!=0:
    print("Search is Successful")
    print("\t {} Found {} Time(s)".format(sp,len(matres)))
else:
    print("Search Un-Successful")
    print("\t {} Not Found".format(sp,len(matres)))