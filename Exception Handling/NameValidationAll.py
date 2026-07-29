#Program for Generating A Name of Word using raise keyword
class SpaceError(Exception):pass
class ZeroNameLengthError(Exception):pass
class InvalidNameError(Exception):pass
def validate_name(n):
    if n.isspace():
        raise SpaceError
    else:
        words=n.split()
        if len(words)==0:
            raise ZeroNameLengthError
        else:
            res=True
            for word in words:
                if not word.isalpha():
                    res=False
                    break
            if res:
                return " ".join(words)
            else:
                raise InvalidNameError
while True:
    try:
        n=input("Enter Any Name: ")
        vname=validate_name(n)
    except InvalidNameError:
        print("\t Do Not Enter Invalid Name---Try Again")
    except ZeroNameLengthError:
        print("\t You Must Enter Your Name---Try Again")
    except SpaceError:
        print("\t Do Not Enter Spaces---Try Again")
    else:
        print("Your Name is {}".format(vname))
        break