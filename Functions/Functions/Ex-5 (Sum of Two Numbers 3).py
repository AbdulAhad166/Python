#program for Defining a Function for adding Two Values
#INPUT          : Taking Input From Function Call (Main Program)
#PROCESS        : Processing Done in Function Body
#RESULT         : Result Displayed in Function Body
def addon(a,b):
    c=a+b
    print("Sum ({},{}) = {}".format(a,b,c))
#Main Program
u=int(input("Enter First Number: "))
e=int(input("Enter Second Number: "))
addon (u,e)