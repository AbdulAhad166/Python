#To display only PYTH without using Indexing and Slicing
s=input("Enter Any String: ")
i=0
while(i<len(s)):
    print("\t {}".format(s[i]))
    i=i+1
else:
    i=0
    while(i<len(s)):
        if s[i]=='o' or s[i]=='O':
            break
        print(s[i],end="")
        i=i+1
    else:
        print("------------------------")
