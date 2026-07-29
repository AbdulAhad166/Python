#Program for swapping of Any two numbers (Don't use Temp var)
#Another Method
a=int(input("Enter the First Value: "))
b=int(input("Enter the Second Value: "))
print("\t Original Value of a={}".format(a))
print("\t Original Value of b={}".format(b))
a=a^b
b=a^b
a=a^b
print("\t Original Value of a={}".format(a))
print("\t Original Value of b={}".format(b))