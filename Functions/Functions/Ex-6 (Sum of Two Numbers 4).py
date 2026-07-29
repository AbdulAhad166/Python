#program for Defining a Function for adding Two Values
#INPUT          : Taking Input Function Body
#PROCESS        : Processing Done in Function Body
#RESULT         : Result Given Back to Function Call (Main Program)
def addon():
    r=float(input("Enter First Number: "))
    s=float(input("Enter Second Number: "))
    d=r+s
    return r,s,d
#Main Program
res=addon()
print("Sum ({},{}) = {}".format(res[0],res[1],res[2])) #Function Call without Input(s) with Single Line assigment
print("------------------OR------------------------")
a,b,c=addon()  #Function Call without Input(s) with Multi Line assigment
print("Sum ({},{}) = {}".format(a,b,c))