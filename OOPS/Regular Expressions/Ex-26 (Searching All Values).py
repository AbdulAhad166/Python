#Program For Searching All Values
import re
gd="BBRSBBRSBBRSBBRSBBRSBBRS"
sp="."
matres=re.finditer(sp,gd)
for mat in matres:
    print("\t Start index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
