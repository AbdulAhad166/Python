#Program for Generating Fibonacci Series using yield keyword in Generator
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        yield a
        c=a+b
        a=b
        b=c
n=int(input("Enter Any Number: "))
for value in fibonacci(n):
    print(value,end=",")