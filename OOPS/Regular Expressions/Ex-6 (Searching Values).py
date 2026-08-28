#Program For Searching all Upper Case Alphabets
import re
gd="Aka6#MpSb8@UrBQg9cRw5Fah"
sp="[A-Z]"
matres=re.finditer(sp,gd)
for mat in matres:
    print("\t Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
