#program for finding whether the give number is positive or negative or zero
num=int(input("Enter Any Number: "))
res="Positive Number" if num>0 else "Negative Number" if num<0 else "Zero"
print(res)