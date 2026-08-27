#Program For Finding The Number of Occurrences For a Word With Different Function names
import re
gd="Python is an oop lang.Python is also Functional Programming Language"
sp="Python"
matres=re.finditer(sp,gd) #Here matres is an object of <class,Callable_Iterator>
for mat in matres:
    print("\t Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
