#Program For Searching the Values Except Lower Case Alphabets
import re
gd="Aka6#MpSb8@UrBQg9cRw5Fah"
sp="[^a-z]"
matres=re.finditer(sp,gd)
for mat in matres:
    print("\t Start index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
