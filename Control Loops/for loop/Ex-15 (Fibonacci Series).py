#Program for generating Fibonacci series using for loop
n=int(input("Enter Any Number: "))
a=0
b=1
for i in range(n):
    print(a,end=",")
    c=a+b
    a=b
    b=c
