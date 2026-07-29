#Program For Accepting Line of Text and Covert Into Upper() and Lower() using Decorators
#Do not use upper() and lower() functions
def lowerconvert(UC):
    def conversion():
        n,uc=UC()
        lc=""
        for ch in n:
            if ord(ch) in range(65,91):
                lc=lc+chr(ord(ch)+32)
            else:
                lc=lc+ch
        return n,uc,lc
    return conversion
def upperconvert(LC):
    def conversion():
        n=LC()
        uc=""
        for ch in n:
            if ord(ch) in range(97,123):
                uc=uc+chr(ord(ch)-32)
            else:
                uc=uc+ch
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
