#program for Defining a Function for adding Two Values Another Method in Functions
#INPUT          : Taking Input Function Body
#PROCESS        : Processing Done in Function Body
#RESULT         : Result Displayed in Function Body
def addon():
    #Take Input in Function
    r=float(input("Enter First Number: "))
    s=float(input("Enter Second Number: "))
    #Process Input
    f=r+s
    #display the result
    print("\tSum ({} ,{})={}".format(r,s,f))
#Main Program
addon()