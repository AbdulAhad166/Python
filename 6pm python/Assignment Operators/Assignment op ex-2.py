#Program for swapping any two numbers without using Temp var
a=int(input("Enter the First value: "))
b=int(input("Enter the Second value: "))
print("\t Original value of a={}".format(a))
print("\t Original value of b={}".format(b))
a=a+b
b=a-b
a=a-b
print("\t Original value of a={}".format(a))
print("\t Originals value of b={}".format(b))