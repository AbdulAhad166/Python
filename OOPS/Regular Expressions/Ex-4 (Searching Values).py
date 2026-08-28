#Program For Searching Either 'a' or 'b' or 'c' Only
import re
gd="Aka6#MpSb8@UrBQg9cRw5Faahhh"
sp="[abc]"
matres=re.finditer(sp,gd)
for mat in matres:
    print("\t Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
    