#Program for Sum of Two Numbers Using a Function
def addon(a, b):
    c=a+b  #here c is local variable
    return c # returns the values outside function
#Main Program
res=addon(2, 3)
print("Sum=",res)