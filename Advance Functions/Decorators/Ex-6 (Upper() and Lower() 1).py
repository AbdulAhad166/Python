#Program For Accepting A Line of Text and Convert Into Upper() and Lower() using Decorators
def lowerconvert(UC):
    def conversion():
        n,uc=UC()
        lc=n.lower()
        return n,uc,lc
    return conversion
def upperconvert(LC):
    def conversion():
        n=LC()
        uc=n.upper()
        return n,uc
    return conversion
@lowerconvert
@upperconvert
def getlines():
    return input("Enter A Line of Text: ")

#Main Program
n,uc,lc=getlines()
print("Given Line of Text= ",n)
print("Upper Case= ",uc)
print("Lower Case= ",lc)
