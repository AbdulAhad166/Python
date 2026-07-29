#PROGRAM FOR ACCEPTING A LINE OF TEXT AND DISPLAY EVERY CHAR
s="PYTHON"
print("By using for loop--Forward Direction without using Index")
for ch in s:
    print("\t {}".format(ch))
print("By using for loop--Backward Direction without using Index")
for ch in s[::-1]:
    print("\t {}".format(ch))
print("By using for loop--Forward Direction with +VE Indices")
for i in range(0,len(s)):
    print("\t {}".format(s[i]))
print("By using for loop--Forward Direction with -VE Indices")
for i in range(-len(s),0):
    print("\t {}".format(s[i]))
print("By using for loop--Back Direction with +VE Indices")
for i in range(len(s)-1,-1,-1):
    print("\t {}".format(s[i]))
print("By using for loop--Back Direction with -VE Indices")
for i in range(-1,len(s),-1):
    print("\t {}".format(s[i]))

