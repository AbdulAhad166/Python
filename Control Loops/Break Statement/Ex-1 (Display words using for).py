#program for Demonstrating the Functionality of break
s=input("Enter Any Value: ")
for ch in s:
    print("\t {}".format(ch))
#To display Only PYTH without using Indexing and Slicing
for ch in s:
    if ch== 'O' or ch=='o':
        break
    else:
        print(ch,end="")
