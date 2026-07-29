#program fo accepting numerical value and change it's sign
num=int(input("Enter Any Number: "))
res=-num if num>0 else abs(num)
print("Changed sign is: ",res)