#Program For Searching All Alphabets
import re
gd="Aka6#MpSb8@UrBQg9cRw5Fah"
sp="[A-Za-z]"
matres=re.finditer(sp,gd)
for mat in matres:
    print("\t Start index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
