#FunctionTest1.py
def welcome(name):
    print("\tHi {}, Welcome to functions".format(name))
#main program
print("I am before Function Call")
print("Type of welcome=",type(welcome))
welcome("Guido") # Function Call
welcome("Travis")# Function Call
print("I am after Function Call")