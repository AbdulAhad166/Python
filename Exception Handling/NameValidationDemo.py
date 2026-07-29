#NameValidationDemo.py<-----Main Program
from NameExcept import ZeroNameLengthError,InvalidNameError,SpaceError
from NameValidation import name
while True:
    try:
        n=input("Enter Any Word: ")
        vname=name(n)
    except ZeroNameLengthError:
        print("\t You Must Enter Your Name---Try Again")
    except InvalidNameError:
        print("\t Do Not Enter Invalid Name---Try Again")
    except SpaceError:
        print("\t Do Not Enter Spaces---Try Again")
    else:
        print("\t Your Name is {}".format(vname))
        break
