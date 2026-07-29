#This is the old version (2.0) of python that uses this __main__
#FunctionTest2.py
def welcome(name):
    print("\tHi {}, Welcome to functions".format(name))

if __name__=="__main__":
    print("I am before Function Call")
    print("Type of welcome=",type(welcome))
    welcome("Guido") # Function Call
    welcome("Travis")# Function Call
    print("I am after Function Call")