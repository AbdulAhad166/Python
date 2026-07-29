#Program for Generating fibonacci Series using list in functions
def fibonacci(n):
    series = []
    a=0
    b=1
    for i in range(n):
        series.append(a)
        c=a+b
        a=b
        b=c
    return series
#Main Program
n=int(input("Enter Any Number: "))
print(fibonacci(n))