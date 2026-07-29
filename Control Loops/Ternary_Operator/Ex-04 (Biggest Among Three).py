#program for accepting three numerical values and find biggest among them
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
c=int(input("Enter Third Number: "))
res="All Numbers are equal" if a == b == c else "a is biggest" if a>=b and a>=c else "b is biggest" if b>=c and b>=a else "c is biggest"
print(res)