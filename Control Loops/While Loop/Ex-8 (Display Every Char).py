#PROGRAM FOR ACCEPTING A LINE OF TEXT AND DISPLAY EVERY CHAR
n=input("Enter a Line Of Text/Word: ")
print("By Using While Loop +VE Indices in Forward Direction")
i=0
while i<len(n):
    print("\t {}".format(n[i]))
    i=i+1
print("By Using While Loop -VE Indices in Forward Direction")
i=-len(n)
while i<=-1:
    print("\t {}".format(n[i]))
    i=i+1
print("By Using While Loop +VE Indices in Backward Direction")
i=len(n)-1
while i>=0:
    print("\t {}".format(n[i]))
    i=i-1
print("By Using While Loop -VE Indices in Backward Direction")
i=-1
while i>=-len(n):
    print("\t {}".format(n[i]))
    i=i-1