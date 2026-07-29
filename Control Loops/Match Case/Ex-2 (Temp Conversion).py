#program for Implementing Temp Conversion Scale
s="""
===================================================
	Temperature Conversion Scale
===================================================
        1. F to C
        2. F to K
        3. C to F
        4. C to K
        5. K to F
        6. K to C
        7. Exit
==================================================="""
print(s)
ch=int(input("Enter Your Choice: "))
match(ch):
    case 1:
        F=float(input("Enter The Temperature in Terms of F: "))
        C=(F - 32) * (5 / 9)
        print("\t Temperature in Terms of C: ",C)
    case 2:
        F=float(input("Enter The Temperature in Terms of F: "))
        K = (F - 32) * (5 / 9) + 273.15
        print("\t Temperature in Terms of K: ",K)
    case 3:
        C=float(input("Enter The Temperature in Terms of C: "))
        F = C * (9 / 5) + 32
        print("\t Temperature in Terms of F: ",F)
    case 4:
        C=float(input("Enter The Temperature in Terms of C: "))
        K = C + 273.15
        print("\t Temperature in Terms of K: ",K)
    case 5:
        K=float(input("Enter The Temperature in Terms of K: "))
        F = (K - 273.15)*(9 / 5) + 32
        print("\t Temperature in Terms of F: ",F)
    case 6:
        K=float(input("Enter The Temperature in Terms of K: "))
        C = K - 273.15
        print("\t Temperature in Terms of C: ",C)
    case 7:
        print("\t Thank you For using this Temperature Conversion Scale")
        exit()
    case _:
        print("\t Invalid Input -- Try Again")