#Program for Demonstrating Global KeyWord
def modify1():
    global a  #Here global is a keyword and to access the local variables we need to use global keyword
    a=a+1
def modify2():
    global a
    a=a*2
#Main Program
a=10   #Here a is global variable
print("Value of a before modify1()=",a)   #10
modify1()
print("Value of a after modify1()=",a)     #11
modify2()
print("Value of a after modify2()=",a)     #22