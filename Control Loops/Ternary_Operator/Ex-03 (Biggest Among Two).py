#program for accepting any numerical value and find it's biggest among them
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
res= "First Number is Biggest" if a>b else "Second Number is Biggest" if b>a else "Both Numbers are Equal"
print(res)