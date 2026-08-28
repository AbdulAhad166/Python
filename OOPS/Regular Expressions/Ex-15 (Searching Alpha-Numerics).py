#Program For Searching the Values Except Alpha-Numerics
import re
gd="Aka6#MpSb8@UrBQg9cRw5Fah"
sp="[^A-Za-z0-9]"
matres=re.finditer(sp,gd)
for mat in matres:
    print("\t Start index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
