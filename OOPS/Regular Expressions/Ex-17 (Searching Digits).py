#Program For Searching Except Digits --- Pre-defined
import re
gd="Aka6#MpSb8@UrBQg9cRw5Fah"
sp=r"\D"   #Pre-Defined
matres=re.finditer(sp,gd)
for mat in matres:
    print("\t Start index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
