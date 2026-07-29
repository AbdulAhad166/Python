#NameValidation.py<---Module Name
from NameExcept import SpaceError,InvalidNameError,ZeroNameLengthError
def name(n):
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