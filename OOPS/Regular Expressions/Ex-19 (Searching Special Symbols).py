#Program For Searching All Special Symbols--- Pre-defined
import re
gd="Aka6#MpSb8@UrBQg9cRw5Fah"
sp=r"\W"   #Pre-Defined
matres=re.finditer(sp,gd)
for mat in matres:
    print("\t Start index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
