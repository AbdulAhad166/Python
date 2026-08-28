#Program for Searching all Word Chars
import re
gd="Aka6#MpSb8@UrBQg9cRw5Fah"
sp=r"\w"
matres=re.finditer(sp,gd)
print("-"*50)
for mat in matres:  # Here mat is an object of <class, re.Match>
	print("\tStart Index:{}   End Index:{}   Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-"*50)