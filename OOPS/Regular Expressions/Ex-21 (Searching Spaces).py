#Program For Searching Except Space Character--- Pre-defined
import re
gd="Aka6 #MpSb8 @UrBQg9 cRw5Fah"
sp=r"\S"   #Pre-Defined
matres=re.finditer(sp,gd)
for mat in matres:
    print("\t Start index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
