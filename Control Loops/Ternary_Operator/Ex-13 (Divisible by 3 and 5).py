#program to check whether a number is divisible by both 3 and 5 using the if..else operator.
num=int(input("Enter a Number: "))
res="Divisible by 3 and 5" if num % 3==0 and num % 5==0 else "Not Divisible by 3 and 5"
print(res)