#program for Implementing all Arithmetic Operation
print("\tArithmetic Operations")
print("\t\t1.Addition")
print("\t\t2.Subtraction")
print("\t\t3.Multiplication")
print("\t\t4.Division")
print("\t\t5.Floor Division")
print("\t\t6. Modulo Division")
print("\t\t7. Exponentiation")
print("\t\t8. Exit")
ch=int(input("Enter Your Choice: "))
match (ch):
    case 1:
        print("Enter Two Values for Addition")
        a,b=float(input()),float(input())
        print("\t Sum({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter Two Values for Substraction")
        a,b=float(input()),float(input())
        print("\t Sub({},{})={}".format(a,b,a-b))
    case 3:
        print("Enter Two Values for Multiplication")
        a,b=float(input()),float(input())
        print("\t Multi({},{})={}".format(a,b,a*b))
    case 4:
        print("Enter Two Values for Division")
        a,b=float(input()),float(input())
        print("\t Div({},{})={}".format(a,b,a/b))
    case 5:
        print("Enter Two Values for Floor Division")
        a,b=float(input()),float(input())
        print("\t Floor({},{})={}".format(a,b,a//b))
    case 6:
        print("Enter Two Values for Modulo Division")
        a,b=float(input()),float(input())
        print("\t Mod({},{})={}".format(a,b,a%b))
    case 7:
        print("Enter Two Values for Exponentiation")
        a,b=float(input()),float(input())
        print("\t Exp({},{})={}".format(a,b,a**b))
    case 8:
        print("Thank you For using this program")
        exit()
    case _:
        print("Invalid Option -- Try Again")
