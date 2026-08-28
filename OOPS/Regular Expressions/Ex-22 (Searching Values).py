#Program For Searching Exactly One Value Only
import re
gd="BBRSBBRSBBRSBBRSBBRSBBRS"
sp="B"
matres=re.finditer(sp,gd)
for mat in matres:
    print("\t Start index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(),mat.group()))
