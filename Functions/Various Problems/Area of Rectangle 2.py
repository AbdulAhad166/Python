#By using Functions, Cal area of Rectangle
#RectAreaCalEx2.py
def readLB():
    L=float(input("Enter Length of Rectangle:"))
    B=float(input("Enter Breadth of Rectangle:"))
    return L,B
def calarea():
    L,B=readLB() # One Function is calling another--Called Function Chain
    ar=L*B
    dispresult(L,B,ar) # One Function is calling another--Called Function Chain
def dispresult(L,B,ar):
    print('----------------------------------')
    print("\tLength=",L)
    print("\tBreadth=",B)
    print("\tArea=",ar)
    print('----------------------------------')
#Main Program
calarea()