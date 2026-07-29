#Write a program to find the smallest of two numbers using the if..else operator
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
res="a is smallest" if a<b else "b is smallest" if b<a else "Both are equal"
print(res)