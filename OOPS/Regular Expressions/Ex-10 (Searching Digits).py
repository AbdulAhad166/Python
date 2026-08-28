#Program For Searching the Digits Only
import re
gd="Aka6#MpSb8@UrBQg9cRw5Fah"
sp="[0-9]"
matres=re.finditer(sp,gd)
for mat in matres:
    print("\t Start index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
