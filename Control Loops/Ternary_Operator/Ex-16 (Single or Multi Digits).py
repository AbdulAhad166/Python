#program to determine whether number is single-digit number or multi-digit number using the if..else operator.
num=int(input("Enter a number: "))
res="Single Digit Number" if -9<=num<=9 else "Multiple Digit Number"
print(res)