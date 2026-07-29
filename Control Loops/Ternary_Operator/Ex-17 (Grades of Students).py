#program to calculate grade of a student (A, B, C, or F) using nested if..else operators.
num=int(input("Enter Your Grade: "))
grade="A Grade" if num>=90 else "B Grade" if num>=70 else "C Grade" if num>=60 else "F Fail"
print(grade)