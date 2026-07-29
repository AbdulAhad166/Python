#Program for Generating Fibonacci Series using Functions
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a,end=",")
        c=a+b
        a=b
        b=c
#Main Program
n=int(input("Enter Any Number: "))
fibonacci(n)