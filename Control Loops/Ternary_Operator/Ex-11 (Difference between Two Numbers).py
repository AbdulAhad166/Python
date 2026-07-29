#program to find the absolute difference between two numbers using the if..else operator.
a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
res= a-b if a>b else b-a
print("Absolute Difference Between two Numbers is: ",res)